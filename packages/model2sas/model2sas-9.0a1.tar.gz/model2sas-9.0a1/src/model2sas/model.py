from typing import Literal, Optional, Callable
from dataclasses import dataclass
from functools import partial
from abc import ABC, abstractmethod

import torch
from torch import Tensor

from . import global_vars
from . import calcfunc
from .calcfunc import complex_increase_argument
from .utils import log


class Model(ABC):
    
    @property
    @abstractmethod
    def maxq(self) -> float:
        """max available |q| value.
        """
    
    @abstractmethod
    def amplitude(self, qx: Tensor, qy: Tensor, qz: Tensor) -> Tensor:
        """Calculate the complex amplitude of reciprocal position (qx,qy,qz).
        Return tensor is the same shape and device as input qx/qy/qz
        """
    
    @abstractmethod
    def intensity(self, qx: Tensor, qy: Tensor, qz: Tensor) -> Tensor:
        """Calculate the intensity of reciprocal position (qx,qy,qz).
        Return tensor is the same shape and device as input qx/qy/qz
        """
    
    @abstractmethod
    def intensity_ave(self, q1d: Tensor, offset: int = 100) -> Tensor:
        """Calculate the orientation averaged intensity of |q| values.
        Return tensor is the same shape and device as input q1d, which
        should be 1D tensor.
        """


@dataclass
class BoundingBox:
    xmin: float
    ymin: float
    zmin: float
    xmax: float
    ymax: float
    zmax: float
    
    def contain(self, x: Tensor, y: Tensor, z: Tensor) -> Tensor:
        return (x>=self.xmin) & (x<=self.xmax) & (y>=self.ymin) & (y<=self.ymax) & (z>=self.zmin) & (z<=self.zmax)
    
    @property
    def lower(self) -> Tensor:
        return torch.tensor((self.xmin, self.ymin, self.zmin), dtype=global_vars.PRECISION)
    
    @property
    def upper(self) -> Tensor:
        return torch.tensor((self.xmax, self.ymax, self.zmax), dtype=global_vars.PRECISION)


@dataclass
class Grid:
    """Equally spaced 3d grid
    """
    x1d: Tensor
    y1d: Tensor
    z1d: Tensor
    value3d: Tensor
    
    def __post_init__(self):
        self.spacing = torch.abs(self.x1d[1] - self.x1d[0]).item()
        self.bounding_box = BoundingBox(
            (self.x1d.min() - self.spacing/2).item(),
            (self.y1d.min() - self.spacing/2).item(),
            (self.z1d.min() - self.spacing/2).item(),
            (self.x1d.max() + self.spacing/2).item(),
            (self.y1d.max() + self.spacing/2).item(),
            (self.z1d.max() + self.spacing/2).item(),
        )
    
    @property
    def coord3d(self) -> tuple[Tensor, Tensor, Tensor]:
        x, y, z = torch.meshgrid(self.x1d, self.y1d, self.z1d, indexing='ij')
        return x, y, z
    
    def interpolate(self, x: Tensor, y: Tensor, z: Tensor) -> Tensor:
        d = self.x1d[1] - self.x1d[0]
        return calcfunc.trilinear_interp(
            x, y, z, self.x1d, self.y1d, self.z1d, self.value3d, d
        )
        
class ReciprocalGrid(Grid):
    """Reciprocal grid that is a centrosymmetric 3D grid
    so only need upper half (z>=0), other half can be
    calculated centrosymmetrically.
    And it's basically (0,0) centered in xy plane
    """
    def interpolate(self, x: Tensor, y: Tensor, z: Tensor) -> Tensor:
        sign = torch.ones_like(z)
        sign[z<0] = -1.
        return super().interpolate(sign*x, sign*y, sign*z)
    
    @property
    def max_radius(self):
        return torch.tensor((self.x1d[0], self.x1d[-1], self.y1d[0], self.y1d[-1], self.z1d[-1])).abs().min()
    
    
class GeoTransforms:
    
    @dataclass
    class Record:
        type: Literal['translate', 'rotate']
        args: tuple
        func_real: Callable
        func_reciprocal: Callable[[Tensor, Tensor, Tensor, Tensor], tuple[Tensor, Tensor, Tensor, Tensor]]
    
    def __init__(self) -> None:
        self.records: list[GeoTransforms.Record] = []
    
    def add_translate(self, vx: float, vy: float, vz: float):
        self.records.append(self.Record(
            'translate',
            (vx, vy, vz),
            partial(self._translate_real, vx, vy, vz),
            partial(self._translate_reciprocal, vx, vy, vz)
        ))
    
    def add_rotate(self, v_axis: tuple[float, float, float], angle: float):
        self.records.append(self.Record(
            'rotate',
            (v_axis, angle),
            partial(self._rotate_real, v_axis, angle),
            partial(self._rotate_reciprocal, v_axis, angle)
        ))
    
    @staticmethod
    def _translate_real(vx, vy, vz, x, y, z, value):
        pass
    
    @staticmethod
    def _translate_reciprocal(vx: float, vy: float, vz: float, qx: Tensor, qy: Tensor, qz: Tensor, complex_argument_addend: Tensor) -> tuple[Tensor, Tensor, Tensor, Tensor]:
        added_arg = -(qx*vx + qy*vy + qz*vz)
        return qx, qy, qz, complex_argument_addend + added_arg
    
    @staticmethod
    def _rotate_real(v_axis, angle, x, y, z, value):
        pass
    
    @staticmethod
    def _rotate_reciprocal(v_axis: tuple[float, float, float], angle: float, qx: Tensor, qy: Tensor, qz: Tensor, complex_argument_addend: Tensor) -> tuple[Tensor, Tensor, Tensor, Tensor]:
        rqx, rqy, rqz = calcfunc.euler_rodrigues_rotate(qx, qy, qz, v_axis, -angle)
        return rqx, rqy, rqz, complex_argument_addend
    
    def apply_real(self):
        pass
    
    def apply_reciprocal(self, qx: Tensor, qy: Tensor, qz: Tensor) -> tuple[Tensor, Tensor, Tensor, Tensor]:
        complex_argument_addend = torch.zeros_like(qx)
        for rcd in reversed(self.records):
            qx, qy, qz, complex_argument_addend = rcd.func_reciprocal(qx, qy, qz, complex_argument_addend)
        return qx, qy, qz, complex_argument_addend
    
    
    
class GridModel(Model):
    
    def __init__(self, x1d: Tensor, y1d: Tensor, z1d: Tensor, sld: Tensor, device: Optional[str|torch.device] = None) -> None:
        if device is None:
            self.device = sld.device
        else:
            self.device = torch.device(device)
        x1d, y1d, z1d, sld = x1d.to(device), y1d.to(device), z1d.to(device), sld.to(device)
        self.real_grid = Grid(x1d, y1d, z1d, sld)
        
        self.transforms = GeoTransforms()
        self.clear_transforms() # add basic translate record for grid centering
        
    def clear_transforms(self):
        self.transforms.records.clear()
        # 由于fft默认网格最左下角的格点在(0,0,0)位置，因此基础就要有一定的平移才是真正的模型散射振幅
        self.translate(
            self.real_grid.bounding_box.xmin + self.real_grid.spacing/2,
            self.real_grid.bounding_box.ymin + self.real_grid.spacing/2,
            self.real_grid.bounding_box.zmin + self.real_grid.spacing/2,
        )
    
    @property
    def sld(self) -> Tensor:
        return self.real_grid.value3d
    
    @property
    def maxq(self) -> float:
        return self.reciprocal_grid.max_radius.item()
    
    @log
    def scatter(self, nq: Optional[int] = None, form_factor: bool = True):
        # determine 1d grid number in reciprocal space
        real_size_max = max(*self.real_grid.x1d.shape, *self.real_grid.y1d.shape, *self.real_grid.z1d.shape)
        if form_factor:
            if nq is None:
                nq = min(600, 10*real_size_max) # in case of using too much resource
            else:
                nq = max(nq, real_size_max)
        else:
            nq = real_size_max
        
        s1d = torch.fft.fftfreq(nq, d=self.real_grid.spacing, device=self.device)
        s1d = torch.fft.fftshift(s1d)
        s1dz = torch.fft.rfftfreq(nq, d=self.real_grid.spacing, device=self.device)
        
        q1d, q1dz = 2*torch.pi*s1d, 2*torch.pi*s1dz
        
        F_half = torch.fft.rfftn(self.real_grid.value3d, s=(nq, nq, nq))
        F_half = torch.fft.fftshift(F_half, dim=(0,1))
        

        ##### Continuous-density correction #####
        # Correct discrete density to continuous density by 
        # multiplying box scattering function from a voxel.
        # And slso eliminate the intensity difference caused by 
        # different spacing in real space.
        d = self.real_grid.spacing
        sinc = lambda t: torch.nan_to_num(torch.sin(t)/t, nan=1.)
        sinc1d, sinc1dz = sinc(q1d*d/2), sinc(q1dz*d/2)
        box_scatt = torch.einsum('i,j,k->ijk', sinc1d, sinc1d, sinc1dz)
        F_half = F_half * d**3 * box_scatt
        
        self.reciprocal_grid = ReciprocalGrid(q1d, q1d, q1dz, F_half)
        
    
    def translate(self, vx: float, vy: float, vz: float):
        self.transforms.add_translate(vx, vy, vz)
    
    def rotate(self, v_axis: tuple[float, float, float], angle: float):
        self.transforms.add_rotate(v_axis, angle)
    
    @log
    def amplitude(self, qx: Tensor, qy: Tensor, qz: Tensor) -> Tensor:
        input_device = qx.device
        qx, qy, qz = qx.to(self.device), qy.to(self.device), qz.to(self.device)
        qx, qy, qz, complex_argument_addend = self.transforms.apply_reciprocal(qx, qy, qz)
        F = self.reciprocal_grid.interpolate(qx, qy, qz)
        F = complex_increase_argument(F, complex_argument_addend)
        return F.to(input_device)
    
    @log
    def intensity(self, qx: Tensor, qy: Tensor, qz: Tensor) -> Tensor:
        F = self.amplitude(qx, qy, qz)
        return F.real**2 + F.imag**2
    
    @log
    def intensity_ave(self, q1d: Tensor, offset: int = 100) -> Tensor:
        q1d_effective = q1d[q1d<=self.maxq]
        N = torch.round(q1d_effective/q1d_effective[0]) + offset
        
        qx, qy, qz = calcfunc.multiple_spherical_sampling(q1d_effective, N)
        
        Iall = self.intensity(qx, qy, qz)
        I = torch.zeros_like(q1d_effective)
        begin = 0
        for i, n in enumerate(N):
            n = n.int().item()
            I[i] = Iall[begin:begin+n].mean()
            begin += n
        
        I1d = torch.zeros_like(q1d)
        I1d[q1d<=self.maxq] = I
        I1d[q1d>self.maxq] = torch.nan
        return I1d


class AssemblyModel(Model):
    
    def __init__(self, *grid_models: 'GridModel|AssemblyModel') -> None:
        self.components = grid_models
        
    @property
    def maxq(self) -> float:
        return min(*[model.maxq for model in self.components])
    
    @log
    def amplitude(self, qx: Tensor, qy: Tensor, qz: Tensor) -> Tensor:
        F = torch.complex(torch.zeros_like(qx), torch.zeros_like(qx))
        for model in self.components:
            F += model.amplitude(qx, qy, qz)
        return F
    
    @log
    def intensity(self, qx: Tensor, qy: Tensor, qz: Tensor) -> Tensor:
        F = self.amplitude(qx, qy, qz)
        return F.real**2 + F.imag**2
    
    @log
    def intensity_ave(self, q1d: Tensor, offset: int = 100) -> Tensor:
        q1d_effective = q1d[q1d<=self.maxq]
        N = torch.round(q1d_effective/q1d_effective[0]) + offset
        
        qx, qy, qz = calcfunc.multiple_spherical_sampling(q1d_effective, N)
        
        Iall = self.intensity(qx, qy, qz)
        I = torch.zeros_like(q1d_effective)
        begin = 0
        for i, n in enumerate(N):
            n = n.int().item()
            I[i] = Iall[begin:begin+n].mean()
            begin += n
        
        I1d = torch.zeros_like(q1d)
        I1d[q1d<=self.maxq] = I
        I1d[q1d>self.maxq] = torch.nan
        return I1d
