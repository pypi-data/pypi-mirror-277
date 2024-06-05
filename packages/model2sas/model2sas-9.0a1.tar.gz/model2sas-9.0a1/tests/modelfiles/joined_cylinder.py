import torch
from torch import Tensor
from model2sas import AbstractMathModel


class MathModel(AbstractMathModel):
    def __init__(self) -> None:
        self.coord = 'cyl'
        
        self.R: float = 10
        self.H: float = 30
        self.sld_value1: float = -1
        self.sld_value2: float = 2
    
    def bounding_box(self):
        return \
            -self.R,   \
            -self.R,   \
            -self.H/2, \
            self.R,    \
            self.R,    \
            self.H/2

    def sld(self, u: Tensor, v: Tensor, w: Tensor) -> Tensor:
        sld = torch.zeros_like(u)
        sld[(u<=self.R)&(w>=-self.H/2)&(w<0)] = self.sld_value1
        sld[(u<=self.R)&(w>=0)&(w<=self.H/2)] = self.sld_value2
        return sld