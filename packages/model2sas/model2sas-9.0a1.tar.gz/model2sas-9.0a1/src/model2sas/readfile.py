from abc import ABC, abstractmethod
from typing import Optional, Literal
from pathlib import Path
import sys

import torch
from torch import Tensor
from stl import mesh
import Bio.PDB
import periodictable as pt
import numpy as np

from . import global_vars
from .model import GridModel, BoundingBox
from . import calcfunc
from .utils import log


@log
def meshgrid(bounding_box: BoundingBox, n_long: int = 50, spacing: Optional[float] = None, device: Optional[str|torch.device] = None, against_edges: bool = False) -> tuple[Tensor, Tensor, Tensor, Tensor, Tensor, Tensor]:
    if device is None:
        device = global_vars.DEFAULT_DEVICE
    
    bbox = bounding_box
    lx, ly, lz = bbox.xmax - bbox.xmin, bbox.ymax - bbox.ymin, bbox.zmax - bbox.zmin
    lmin, lmax = min(lx, ly, lz), max(lx, ly, lz)
    
    if spacing is None:
        spacing = lmax / n_long
        spacing = min(spacing, lmin/10) # in case of too few points in short edge
    
    eps = spacing * 1e-3
    if against_edges:
        x1d = torch.arange(bbox.xmin, bbox.xmax+spacing+eps, spacing, dtype=global_vars.PRECISION, device=device)
        y1d = torch.arange(bbox.ymin, bbox.ymax+spacing+eps, spacing, dtype=global_vars.PRECISION, device=device)
        z1d = torch.arange(bbox.zmin, bbox.zmax+spacing+eps, spacing, dtype=global_vars.PRECISION, device=device)
    else:
        x1d = torch.arange(bbox.xmin+spacing/2, bbox.xmax+spacing/2+eps, spacing, dtype=global_vars.PRECISION, device=device)
        y1d = torch.arange(bbox.ymin+spacing/2, bbox.ymax+spacing/2+eps, spacing, dtype=global_vars.PRECISION, device=device)
        z1d = torch.arange(bbox.zmin+spacing/2, bbox.zmax+spacing/2+eps, spacing, dtype=global_vars.PRECISION, device=device)
    x, y, z = torch.meshgrid(x1d, y1d, z1d, indexing='ij')
    return x1d, y1d, z1d, x, y, z




class AbstractMathModel(ABC):
    """Parameter name obeys python var name protocal.
    Must have:
        coord: Literal['car', 'sph', 'cyl']
    Must avoid: 
        filename, filename_or_class, sld_value, 
        centering, n_long, spacing, device
    """
    @abstractmethod
    def __init__(self) -> None:
        """Define coord and other params here.
        """
        
    def update_params(self, **kwargs) -> None:
        self.__dict__.update(**kwargs)
    
    @abstractmethod
    def bounding_box(self) -> tuple[float, float, float, float, float, float]:
        """re-generate boundary for every method call
        in case that params are altered in software.
        return coordinates in Cartesian coordinates.

        Returns:
            tuple[float, float, float, float, float, float]: xmin, ymin, zmin, xmax, ymax, zmax
        """
    
    @abstractmethod
    def sld(self, u: Tensor, v: Tensor, w: Tensor) -> Tensor:
        """Calculate sld values of certain coordinates.
        u, v, w means:
        x, y, z if self.coord=='car';
        r, theta, phi if self.coord=='sph';
        rho, theta, z if self.coord=='cyl';

        Args:
            u (Tensor): 1st coord
            v (Tensor): 2nd coord
            w (Tensor): 3rd coord

        Returns:
            Tensor: sld values of each coordinates
        """


def import_mathmodel_class(filename: str | Path):
    filename = Path(filename)
    sys.path.append(str(filename.absolute().parent))
    module = __import__(filename.stem)
    mathmodel_class = module.MathModel
    return mathmodel_class


@log
def read_math(
    filename_or_mathmodel: str|AbstractMathModel,
    n_long: int = 50,
    spacing: Optional[float] = None,
    device: Optional[str|torch.device] = None,
    **mathmodel_params,
    ) -> GridModel:
    if device is None:
        device = global_vars.DEFAULT_DEVICE
    if isinstance(filename_or_mathmodel, str):
        filename = filename_or_mathmodel
        MathModel = import_mathmodel_class(filename)
        mathmodel = MathModel()
    else:
        mathmodel = filename_or_mathmodel
    
    mathmodel.update_params(**mathmodel_params)
    
    bounding_box = BoundingBox(*mathmodel.bounding_box())
    x1d, y1d, z1d, x, y, z = meshgrid(bounding_box, n_long=n_long, spacing=spacing, device=device)
        
    u, v, w = calcfunc.convert_coord(x, y, z, 'car', mathmodel.coord)
    sld = mathmodel.sld(u, v, w)
    
    return GridModel(x1d, y1d, z1d, sld, device=device)


@log
def read_stl(
    filename: str,
    sld_value: int = 1,
    centering: bool = False,
    n_long: int = 50,
    spacing: Optional[float] = None,
    device: Optional[str|torch.device] = None
    ) -> GridModel:
    if device is None:
        device = global_vars.DEFAULT_DEVICE
    
    stlmesh = mesh.Mesh.from_file(filename)
    
    if centering:# move model center to (0,0,0)
        center = stlmesh.get_mass_properties()[1]
        stlmesh.translate(-center)
    
    vec = stlmesh.vectors
    vec = vec.reshape((vec.shape[0]*vec.shape[1], vec.shape[2]))
    bboxmin, bboxmax = vec.min(axis=0), vec.max(axis=0)
    bounding_box = BoundingBox(*bboxmin, *bboxmax)
    
    x1d, y1d, z1d, x, y, z = meshgrid(bounding_box, n_long=n_long, spacing=spacing, device=device)
    
    # check inside model by ray intersect
    points = torch.stack((x, y, z), dim=-1)
    ray = torch.rand(3, dtype=global_vars.PRECISION, device=device) - 0.5
    triangles = torch.from_numpy(stlmesh.vectors.copy()).to(global_vars.PRECISION).to(device)
    intersect_count = calcfunc.moller_trumbore_intersect_count(points, ray, triangles)
    
    index = intersect_count % 2   # 1 is in, 0 is out
    sld = sld_value * index
    sld = sld.reshape(x.shape)

    return GridModel(x1d, y1d, z1d, sld, device=device)


@log
def read_pdb(
    filename: str,
    probe: Literal['xray', 'neutron'] = 'xray',
    wavelength: float = 1.54,
    n_long: int = 50,
    spacing: Optional[float] = None,
    device: Optional[str|torch.device] = None
    ) -> GridModel:
    """与stl，math的区别在于pdb模型中格点处就代表一个原子，
    所以meshgrid要贴边生成。
    """
    if device is None:
        device = global_vars.DEFAULT_DEVICE
    
    # slowest part
    pdbparser = Bio.PDB.PDBParser(QUIET=True)   # suppress PDBConstructionWarning
    pdb_structure = pdbparser.get_structure(Path(filename).stem, filename)
    
    if probe == 'neutron':
        atom_f_func = lambda pt_element: pt_element.neutron.b_c
    else:
        atom_f_func = lambda pt_element: pt_element.xray.scattering_factors(wavelength=wavelength)[0]
    
    # second slowest, but bottlenetck should be pdb_structure.get_atoms()?
    atom_f = torch.tensor(
        [atom_f_func(pt.elements.symbol(atom.element.capitalize())) for atom in pdb_structure.get_atoms()],
        dtype=global_vars.PRECISION, device=device
    )
    atom_coord = torch.from_numpy(
        np.stack([atom.coord for atom in pdb_structure.get_atoms()], axis=0)
    ).to(global_vars.PRECISION).to(device)
    
    bounding_box = BoundingBox(
        *(atom_coord.min(dim=0).values).tolist(),
        *(atom_coord.max(dim=0).values).tolist(),
    )
    x1d, y1d, z1d, x, y, z = meshgrid(bounding_box, n_long=n_long, spacing=spacing, device=device, against_edges=True)
    
    actual_spacing = x1d[1] - x1d[0]
    index = (atom_coord - bounding_box.lower.to(device)) / actual_spacing
    index = index.round().to(torch.int64)
    sld = torch.zeros_like(x)
    sld[index[:,0], index[:,1], index[:,2]] += atom_f # in case that multiple atoms in one voxel
    
    return GridModel(x1d, y1d, z1d, sld, device=device)
