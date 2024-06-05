"""some useful utility functions
"""

from typing import Literal
import time
import sys
import functools

import torch
from torch import Tensor
from loguru import logger

from . import global_vars


func_tier: int = 0
    
def add_logger(sink=sys.stderr, format=global_vars.LOG_FORMAT_STR, **kwargs):
    logger.add(sink, format=format, **kwargs)
    
logger.remove(0)
logger.add(sys.stderr, format=global_vars.LOG_FORMAT_STR)

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if global_vars.PRINT_LOG:
            global func_tier
            if global_vars.LOG_LEVEL<0 or func_tier<=global_vars.LOG_LEVEL:
                logger.info(f'[{" ":>11}] {"|  "*func_tier}○ {func.__name__}')
            func_tier += 1
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            time_cost = time.perf_counter() - start_time
            func_tier -= 1
            if global_vars.LOG_LEVEL<0 or func_tier<=global_vars.LOG_LEVEL:
                logger.success(f'[{time_cost:>9.6f} s] {"|  "*func_tier}● {func.__name__}')
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper


class Detector:
    '''Simulation of a 2d detector.
    In a coordinate system where sample position as origin,
    beam direction as positive Y axis.
    All length unit should be meter except wavelength.
    Output q unit will be reverse wavelength unit.
    '''
    def __init__(self, resolution: tuple[int, int], pixel_size: float) -> None:
        x = torch.arange(resolution[0], dtype=torch.float32)
        z = torch.arange(resolution[1], dtype=torch.float32)
        x, z = pixel_size*x, pixel_size*z
        cx, cz = (x[0]+x[-1])/2, (z[0]+z[-1])/2
        x, z = x - cx, z - cz
        x, z = torch.meshgrid(x, z, indexing='ij')
        y = torch.zeros_like(x, dtype=torch.float32)
        self.x, self.y, self.z = x, y, z
        self.pitch_axis = torch.tensor((1,0,0), dtype=torch.float32)
        self.yaw_axis = torch.tensor((0,0,1), dtype=torch.float32)
        self.roll_axis = torch.tensor((0,1,0), dtype=torch.float32)
        self.sdd = 0.
        self.resolution = resolution
        self.pixel_size = pixel_size

    def get_center(self) -> Tensor:
        cx = (self.x[0,0] + self.x[-1,-1]) / 2
        cy = (self.y[0,0] + self.y[-1,-1]) / 2
        cz = (self.z[0,0] + self.z[-1,-1]) / 2
        return torch.tensor((cx, cy, cz))

    def set_sdd(self, sdd: float) -> None:
        delta_sdd = sdd - self.sdd
        self.y = self.y + delta_sdd
        self.sdd = sdd

    def translate(self, vx: float, vz: float, vy: float = 0.) -> None:
        self.x = self.x + vx
        self.z = self.z + vz
        self.y = self.y + vy
        self.sdd = self.sdd + vy

    def _euler_rodrigues_rotate(self, coord: Tensor, axis: Tensor, angle: float) -> Tensor:
        '''Rotate coordinates by euler rodrigues rotate formula.
        coord.shape = (n,3)
        '''
        ax = axis / torch.sqrt(torch.sum(axis**2))
        ang = torch.tensor(angle)
        a = torch.cos(ang/2)
        w = ax * torch.sin(ang/2)

        x = coord
        wx = -torch.linalg.cross(x, w.expand_as(x), dim=-1)
        x_rotated = x + 2*a*wx + 2*(-torch.linalg.cross(wx, w.expand_as(wx), dim=-1))
        return x_rotated

    def _rotate(self, rotation_type: Literal['pitch', 'yaw', 'roll'], angle: float) -> None:
        if rotation_type == 'pitch':
            axis = self.pitch_axis
            self.yaw_axis = self._euler_rodrigues_rotate(self.yaw_axis, axis, angle)
            self.roll_axis = self._euler_rodrigues_rotate(self.roll_axis, axis, angle)
        elif rotation_type == 'yaw':
            axis = self.yaw_axis
            self.pitch_axis = self._euler_rodrigues_rotate(self.pitch_axis, axis, angle)
            self.roll_axis = self._euler_rodrigues_rotate(self.roll_axis, axis, angle)
        elif rotation_type == 'roll':
            axis = self.roll_axis
            self.pitch_axis = self._euler_rodrigues_rotate(self.pitch_axis, axis, angle)
            self.yaw_axis = self._euler_rodrigues_rotate(self.yaw_axis, axis, angle)
        else:
            raise ValueError('Unsupported rotation type: {}'.format(rotation_type))
        center = self.get_center()

        x1d, y1d, z1d = self.x.flatten(), self.y.flatten(), self.z.flatten()
        coord = torch.stack((x1d, y1d, z1d), dim=1)
        coord = coord - center
        rotated_coord = self._euler_rodrigues_rotate(
            coord, axis, angle
        )
        rotated_coord = rotated_coord + center
        x, y, z = torch.unbind(rotated_coord, dim=-1)
        self.x, self.y, self.z = x.reshape(self.resolution), y.reshape(self.resolution), z.reshape(self.resolution)

    def pitch(self, angle: float) -> None:
        self._rotate('pitch', angle)

    def yaw(self, angle: float) -> None:
        self._rotate('yaw', angle)

    def roll(self, angle: float) -> None:
        self._rotate('roll', angle)

    def _real_coord_to_reciprocal_coord(self, x: Tensor, y: Tensor, z: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        '''In a coordinate system where sample position as origin,
        beam direction as positive Y axis, calculate the corresponding
        reciprocal coordinates (without multiply wave vector
        k=2pi/wavelength) by coordinates (x,y,z) in this space.
        '''
        mod = torch.sqrt(x**2 + y**2 + z**2)
        unit_vector_ks_x, unit_vector_ks_y, unit_vector_ks_z = x/mod, y/mod, z/mod
        unit_vector_ki_x, unit_vector_ki_y, unit_vector_ki_z = 0., 1., 0.
        rx = unit_vector_ks_x - unit_vector_ki_x
        ry = unit_vector_ks_y - unit_vector_ki_y
        rz = unit_vector_ks_z - unit_vector_ki_z
        return rx, ry, rz

    def get_reciprocal_coord(self, wavelength: float) -> tuple[Tensor, Tensor, Tensor]:
        k = 2*torch.pi / wavelength
        rx, ry, rz = self._real_coord_to_reciprocal_coord(self.x, self.y, self.z)
        qx, qy, qz = k*rx, k*ry, k*rz
        return qx, qy, qz

    def get_q_range(self, wavelength: float) -> tuple[float, float]:
        qx, qy, qz = self.get_reciprocal_coord(wavelength)
        q = torch.sqrt(qx**2 + qy**2 + qz**2)
        return q.min().item(), q.max().item()

    def get_beamstop_mask(self, d: float) -> Tensor:
        '''pattern must have the same shape as self.x, y, z
        '''
        mask = torch.ones(self.resolution, dtype=torch.float32)
        mask[(self.x**2+self.z**2) <= (d/2)**2] = 0.
        return mask


# 发现用Bio.PDB里的功能保存的pdb文件crysol读取出错，所以还是只能直接写文件
def save_pdb(filename: str, x: Tensor, y: Tensor, z:Tensor, sld: Tensor, atom_name: str = 'CA', temperature_factor: float = 0.0, element_symbol: str = 'C') -> None:
    """Convert a lattice model to a pdb file
    for calculation by other software like CRYSOL.
    Only preserve sld!=0 points with uniform sld value.

    Args:
        x (Tensor): x coordinates
        y (Tensor): x coordinates
        z (Tensor): x coordinates
        sld (Tensor): sld values at each coordinates
        filename (str): output pdb file name
    """    
    sld = sld.flatten()
    x = x.flatten()[sld!=0.]
    y = y.flatten()[sld!=0.]
    z = z.flatten()[sld!=0.]
    sld = sld[sld!=0]
    
    lines = ['REMARK 265 EXPERIMENT TYPE: THEORETICAL MODELLING\n']
    for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
        lines.append(
            f'{"ATOM":<6}{i+1:>5d} {atom_name:<4} {"ASP":>3} {"A":>1}{1:>4d}    {xi:>8.3f}{yi:>8.3f}{zi:>8.3f}{1.0:>6.2f}{temperature_factor:>6.2f}          {element_symbol:>2}  \n'
        )
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
