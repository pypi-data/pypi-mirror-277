"""Compute-related functions in model2sas.
All based on pytorch instead of numpy.
"""

from typing import Literal
import math

import torch
from torch import Tensor

from .utils import log
from . import global_vars


class __CoordConverter:
    """Pre-store the according functions.
    """
    def __init__(self) -> None:
        self.convert_func = {
            'car2car': self.nochange,
            'car2sph': self.car2sph,
            'car2cyl': self.car2cyl,
            'sph2car': self.sph2car,
            'sph2sph': self.nochange,
            'sph2cyl': lambda a, b, c: self.car2cyl(*self.sph2car(a, b, c)),
            'cyl2car': self.cyl2car,
            'cyl2sph': lambda a, b, c: self.car2sph(*self.cyl2car(a, b, c)),
            'cyl2cyl': self.nochange,
        }
    
    # @log
    def __call__(self, u:Tensor, v:Tensor, w:Tensor, original_coord: Literal['car', 'sph', 'cyl'], target_coord: Literal['car', 'sph', 'cyl']) -> tuple[Tensor, Tensor, Tensor]:
        return self.convert_func[f'{original_coord}2{target_coord}'](u, v, w)
    
    @staticmethod
    def nochange(u:Tensor, v:Tensor, w:Tensor) -> tuple[Tensor, Tensor, Tensor]:
        return u, v, w
    @staticmethod
    def car2sph(x:Tensor, y:Tensor, z:Tensor) -> tuple[Tensor, Tensor, Tensor]:
        r = torch.sqrt(x**2 + y**2 + z**2)
        phi = torch.arccos(z/r) # when r=0, output phi=nan
        phi = torch.nan_to_num(phi, nan=0.) # convert nan to 0
        theta = torch.arctan2(y, x) # range [-pi, pi]
        theta = torch.where(theta<0, theta+2*torch.pi, theta) # convert range to [0, 2pi]
        return r, theta, phi
    @staticmethod
    def car2cyl(x:Tensor, y:Tensor, z:Tensor) -> tuple[Tensor, Tensor, Tensor]:
        rho = torch.sqrt(x**2+y**2)
        theta = torch.arctan2(y, x) # range [-pi, pi]
        theta = theta + (1-torch.sign(torch.sign(theta)+1))*2*torch.pi # convert range to [0, 2pi]
        return rho, theta, z
    @staticmethod
    def sph2car(r:Tensor, theta:Tensor, phi:Tensor) -> tuple[Tensor, Tensor, Tensor]:
        sinphi = torch.sin(phi)
        x = r * torch.cos(theta) * sinphi
        y = r * torch.sin(theta) * sinphi
        z = r * torch.cos(phi)
        return x, y, z
    @staticmethod
    def cyl2car(rho:Tensor, theta:Tensor, z:Tensor) -> tuple[Tensor, Tensor, Tensor]:
        x = rho * torch.cos(theta)
        y = rho * torch.sin(theta)
        return x, y, z


# use just like a function
convert_coord = __CoordConverter()


@log
def moller_trumbore_intersect_count(points: Tensor, ray: Tensor, triangles: Tensor) -> Tensor:
    """Calculate all the points intersect with all triangles seperately
    using Möller-Trumbore intersection algorithm.
    See paper https://doi.org/10.1080/10867651.1997.10487468 
    All variable names follow this paper.

    Args:
        points (Tensor): shape=(n1, ..., ni, 3), 3D meshgrid points coordinates
        ray (Tensor): shape=(3,)
        triangles (Tensor): shape=(m, 3, 3), m triangles with 3 vertices, each (3,) coordinates

    Returns:
        Tensor: shape=(n1, ..., ni), indicate intersect counts per point
    """
    #* Highest performance for now, especially on GPU.
    #* No using python loops.
    
    O = points                  # (n1, ..., ni, 3)
    D = ray                     # (3,)
    V0 = triangles[:,0,:]       # (m, 3)
    E1 = triangles[:,1,:] - V0  # (m, 3)
    E2 = triangles[:,2,:] - V0  # (m, 3)
    
    points_coord_dim = (1,) * (O.dim()-1)  # to support any input shape
    
    T = O.unsqueeze(-2) - V0.view(*points_coord_dim, *V0.shape) # (n1, ..., ni, m, 3)
    P = torch.linalg.cross(D.unsqueeze(0), E2, dim=-1) # (m, 3)
    Q = torch.linalg.cross(T, E1.view(*points_coord_dim, *E1.shape), dim=-1) # (n1, ..., ni, m, 3)
    
    PE1_reciprocal = 1 / torch.linalg.vecdot(P, E1, dim=-1) # (m,)
    QE2 = torch.linalg.vecdot(Q, E2.view(*points_coord_dim, *E2.shape), dim=-1) # (n1, ..., ni, m)
    PT = torch.linalg.vecdot(P.view(*points_coord_dim, *P.shape), T, dim=-1) # (n1, ..., ni, m)
    QD = torch.linalg.vecdot(Q, D, dim=-1) # (n1, ..., ni, m)
    
    PE1_reciprocal = PE1_reciprocal.view(*points_coord_dim, *PE1_reciprocal.shape) # (1, 1, 1, m)
    t = PE1_reciprocal * QE2 # (n1, ..., ni, m)
    u = PE1_reciprocal * PT # (n1, ..., ni, m)
    v = PE1_reciprocal * QD # (n1, ..., ni, m)
    
    intersect = torch.zeros_like(t, dtype=torch.int32)
    intersect[(t>0) & (u>0) & (v>0) & ((u+v)<1)] = 1 # (n1, ..., ni, m)
    intersect_count = intersect.sum(-1) # (n1, ..., ni)
    return intersect_count



@log
def complex_increase_argument(complex: Tensor, argument_addend: Tensor|float) -> Tensor:
    """Args:
        complex (Tensor): complex dtype tensor
        argument_addend (Tensor): same shape as complex, or a float apply to all

    Returns:
        Tensor: complex dtype tensor
    """
    mod, arg = torch.sqrt(complex.real**2 + complex.imag**2), torch.arctan2(complex.imag, complex.real)
    arg = arg + argument_addend
    return mod * torch.complex(torch.cos(arg), torch.sin(arg))


# @log
# def nearest_interp(x:Tensor, y:Tensor, z:Tensor, px:Tensor, py:Tensor, pz:Tensor, c:Tensor, d:float | Tensor) -> Tensor:
#     """Conduct nearest interpolate on equally spaced meshgrid.
#     当网格值c是复数时等效于对实部和虚部分别进行插值

#     Args:
#         x (Tensor): any shape, x coordinates of points to be interpolated
#         y (Tensor): any shape, y coordinates of points to be interpolated
#         z (Tensor): any shape, z coordinates of points to be interpolated
#         px (Tensor): shape=(m1,), x1d grid of meshgrid with known values
#         py (Tensor): shape=(m2,), y1d grid of meshgrid with known values
#         pz (Tensor): shape=(m3,), z1d grid of meshgrid with known values
#         c (Tensor): shape=(m1, m2, m3), values of each of in meshgrid(px, py, pz)
#         d (float | Tensor): spacing of meshgrid(px, py, pz), equally spaced

#     Returns:
#         Tensor: same shape as x|y|z, interpolated values of (x, y, z)
#     """
#     ix, iy, iz = (x-px[0]+d/2)/d, (y-py[0]+d/2)/d, (z-pz[0]+d/2)/d
#     ix, iy, iz = ix.to(torch.int64), iy.to(torch.int64), iz.to(torch.int64) # tensors used as indices must be long, byte or bool tensors
#     c_interp = c[ix, iy, iz]
#     return c_interp

@log
def trilinear_interp(x:Tensor, y:Tensor, z:Tensor, px:Tensor, py:Tensor, pz:Tensor, c:Tensor, d:float | Tensor) -> Tensor:
    """Conduct trilinear interpolate on equally spaced meshgrid.
    当网格值c是复数时等效于对实部和虚部分别进行插值

    Args:
        x (Tensor): any shape, x coordinates of points to be interpolated
        y (Tensor): any shape, y coordinates of points to be interpolated
        z (Tensor): any shape, z coordinates of points to be interpolated
        px (Tensor): shape=(m1,), x1d grid of meshgrid with known values
        py (Tensor): shape=(m2,), y1d grid of meshgrid with known values
        pz (Tensor): shape=(m3,), z1d grid of meshgrid with known values
        c (Tensor): shape=(m1, m2, m3), values of each of in meshgrid(px, py, pz)
        d (float | Tensor): spacing of meshgrid(px, py, pz), equally spaced

    Returns:
        Tensor: same shape as x|y|z, interpolated values of (x, y, z)
    """
    ix, iy, iz = (x-px[0])/d, (y-py[0])/d, (z-pz[0])/d
    ix, iy, iz = ix.to(torch.int64), iy.to(torch.int64), iz.to(torch.int64) # tensors used as indices must be long, byte or bool tensors

    x0, y0, z0 = px[ix], py[iy], pz[iz]
    x1, y1, z1 = px[ix+1], py[iy+1], pz[iz+1]
    xd, yd, zd = (x-x0)/(x1-x0), (y-y0)/(y1-y0), (z-z0)/(z1-z0)
    
    c_interp = c[ix, iy, iz]*(1-xd)*(1-yd)*(1-zd) \
        + c[ix+1, iy, iz]*xd*(1-yd)*(1-zd)  \
        + c[ix, iy+1, iz]*(1-xd)*yd*(1-zd)  \
        + c[ix, iy, iz+1]*(1-xd)*(1-yd)*zd  \
        + c[ix+1, iy, iz+1]*xd*(1-yd)*zd    \
        + c[ix, iy+1, iz+1]*(1-xd)*yd*zd    \
        + c[ix+1, iy+1, iz]*xd*yd*(1-zd)    \
        + c[ix+1, iy+1, iz+1]*xd*yd*zd
    return c_interp


@log
def euler_rodrigues_rotate(x: Tensor, y: Tensor, z: Tensor, v_axis: tuple[float, float, float], angle: float) -> tuple[Tensor, Tensor, Tensor]:
    """Central rotation of coordinates by Euler-Rodrigues formula.
    Refer to https://en.wikipedia.org/wiki/Euler%E2%80%93Rodrigues_formula

    Args:
        x (Tensor): any shape, x coordinates of points to be rotated 
        y (Tensor): any shape, y coordinates of points to be rotated 
        z (Tensor): any shape, z coordinates of points to be rotated 
        v_axis (tuple[float, float, float]): axis of rotation
        angle (float): in radian

    Returns:
        tuple[Tensor, Tensor, Tensor]: rotated coordinated rx, ry, yz, same shape and device as input.
    """    
    l = math.dist(v_axis, (0,0,0))
    
    a = math.cos(angle/2)
    b = v_axis[0]/l * math.sin(angle/2) # axis vector should be unit vector
    c = v_axis[1]/l * math.sin(angle/2)
    d = v_axis[2]/l * math.sin(angle/2)
    
    # below is faster than vector formulation by my test    
    rx = (a**2 + b**2 - c**2 - d**2) * x \
        +(2*(b*c - a*d)) * y \
        +(2*(b*d + a*c)) * z
    
    ry = (2*(b*c + a*d)) * x \
        +(a**2 + c**2 - b**2 - d**2) * y \
        +(2*(c*d - a*b)) * z
    
    rz = (2*(b*d - a*c)) * x \
        +(2*(c*d + a*b)) * y \
        +(a**2 + d**2 - b**2 - c**2) * z
    
    return rx, ry, rz


@log
def multiple_spherical_sampling(Rs: Tensor, Ns: Tensor) -> tuple[Tensor, Tensor, Tensor]:
    """Generate sampling points using fibonacci grid
    for multiple spherical shells. r and N are 1D tensor
    with same shape.

    Args:
        r (Tensor): radius of spherical shells
        N (Tensor): number of points on each shell

    Returns:
        tuple[Tensor, Tensor, Tensor]: x, y, z coordinates
    """
    
    # for better performance:
    # lesser loop, lesser work inside loop
    def gen_nNr(R, N):
        n = torch.arange(1, N+1, dtype=global_vars.PRECISION)
        N = torch.full_like(n, N)
        r = torch.full_like(n, R)
        return n, N, r
    nNr = [gen_nNr(R, N) for R, N in zip(Rs, Ns)]
    n = torch.cat([t[0] for t in nNr])
    N = torch.cat([t[1] for t in nNr])
    r = torch.cat([t[2] for t in nNr])
    
    phi = (torch.sqrt(torch.tensor(5, dtype=global_vars.PRECISION))-1)/2
    z = ((2*n-1)/N - 1)
    x = r * torch.sqrt(1-z**2) * torch.cos(2*torch.pi*n*phi)
    y = r * torch.sqrt(1-z**2) * torch.sin(2*torch.pi*n*phi)
    z = r * z
    return x, y, z

    

