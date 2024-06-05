"""
A template of hollow sphere math model
with various sld equal to the x coordinate of certain point

# ! Do not change the class name and method name !
"""

import torch
from torch import Tensor
from model2sas import AbstractMathModel


class MathModel(AbstractMathModel):
    '''to generate a 3D model from a mathematical description.
    For example: a spherical shell is "x**2+y**2+z**2 >= R_core**2 and x**2+y**2+z**2 <= (R_core+thickness)**2
    also, in spherical coordinates, a hollow sphere is (r >= R_core) and (r <= R_core+thickness)

    coord:
    - 'car' in (x, y, z)
    - 'sph' in (r, theta, phi), theta: [0, 2pi) ; phi: [0, pi)
    - 'cyl' in (rho, theta, z), theta: [0, 2pi)
    '''
    
    def __init__(self) -> None:
        """Define coord and other params here.
        """
        self.coord = 'cyl'
        
        self.R: float = 10
        self.H: float = 30
        self.sld_value: float = 1
    
    def bounding_box(self):
        """re-generate boundary for every method call
        in case that params are altered in software.
        return coordinates in Cartesian coordinates.

        Returns:
            tuple[float, float, float, float, float, float]: xmin, ymin, zmin, xmax, ymax, zmax
        """
        return \
            -self.R,   \
            -self.R,   \
            -self.H/2, \
            self.R,    \
            self.R,    \
            self.H/2

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
        # u, v, w is r, theta, phi here for 'sph' coordinates
        sld = torch.zeros_like(u)
        sld[(u<=self.R)&(w>=-self.H/2)&(w<=self.H/2)] = self.sld_value
        return sld