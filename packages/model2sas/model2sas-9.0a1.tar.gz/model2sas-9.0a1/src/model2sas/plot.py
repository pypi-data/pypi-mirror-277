"""All kinds of plot, from 1d to 3d.
"""

from pathlib import Path
from typing import Literal, Optional, Sequence

import torch
from torch import Tensor

import plotly.graph_objects as go


class Voxel(go.Mesh3d):
    def __init__(self, xc=None, yc=None, zc=None, spacing=None, **kwargs):
        x, y, z, i, j, k = self.gen_vertices_triangles(xc, yc, zc, spacing)
        super().__init__(x=x, y=y, z=z, i=i, j=j, k=k, **kwargs)

    def gen_vertices_triangles(self, xc, yc, zc, spacing) -> tuple[Tensor, Tensor, Tensor, Tensor, Tensor, Tensor]:
        """Generate vertices and triangles for mesh plot.
        For each point (xc, yc, zc), generate a cubic box with edge_length = spacing

        Args:
            xc: x coordinates of center point
            yc: y coordinates of center point
            zc: z coordinates of center point
            spacing: spacing of mesh grid, and cubic box edge length

        Returns:
            tuple[Tensor, Tensor, Tensor, Tensor, Tensor, Tensor]: _description_
        """
        s = spacing
        xv = torch.stack((xc-s/2, xc+s/2, xc+s/2, xc-s/2, xc-s/2, xc+s/2, xc+s/2, xc-s/2), dim=1).flatten()
        yv = torch.stack((yc-s/2, yc-s/2, yc+s/2, yc+s/2, yc-s/2, yc-s/2, yc+s/2, yc+s/2), dim=1).flatten()
        zv = torch.stack((zc-s/2, zc-s/2, zc-s/2, zc-s/2, zc+s/2, zc+s/2, zc+s/2, zc+s/2), dim=1).flatten()

        i0 = torch.tensor((0, 2, 0, 5, 1, 6, 2, 7, 3, 4, 4, 6))
        j0 = torch.tensor((1, 3, 1, 4, 2, 5, 3, 6, 0, 7, 5, 7))
        k0 = torch.tensor((2, 0, 5, 0, 6, 1, 7, 2, 4, 3, 6, 4))
        seq = 8 * torch.arange(xc.numel())
        i = (torch.unsqueeze(i0, 0) + torch.unsqueeze(seq, 1)).flatten()
        j = (torch.unsqueeze(j0, 0) + torch.unsqueeze(seq, 1)).flatten()
        k = (torch.unsqueeze(k0, 0) + torch.unsqueeze(seq, 1)).flatten()
        return xv, yv, zv, i, j, k


class Figure(go.Figure):
    
    def __init__(self, data=None, layout=None, frames=None, skip_invalid=False, **kwargs):
        super().__init__(data, layout, frames, skip_invalid, **kwargs)
        
    def write_html(self, filename: str, *args, **kwargs):
        Path(filename).write_text(self.to_html(), encoding='utf-8')
        
    def set_title_text(self, text: str):
        self.update_layout(title_text=text)
        
    def set_template(self, plotly_template: str):
        self.update_layout(template=plotly_template)
    
    @staticmethod
    def __ensure_cpu_tensor(*t):
        if len(t) == 1:
            return t[0].cpu() if isinstance(t[0], Tensor) else t[0]
        else:
            return tuple(ti.cpu() if isinstance(ti, Tensor) else ti for ti in t)
        
    
    def plot_curve1d(self, x: Sequence|Tensor, y: Sequence|Tensor, name: Optional[str] = None, mode: Optional[Literal['lines', 'markers', 'lines+markers']] = None, logx: bool = True, logy: bool = True, **kwargs) -> None:
        x, y = self.__ensure_cpu_tensor(x, y)
        self.add_trace(go.Scatter(x=x, y=y, name=name, mode=mode, **kwargs))
        if logx:
            self.update_xaxes(type='log')
        if logy:
            self.update_yaxes(type='log')
    
    
    def plot_surface2d(self, data2d: Tensor, log_value: bool = True, colorscale: Optional[str] = None) -> None:
        data2d = self.__ensure_cpu_tensor(data2d)
        if log_value:
            data2d = torch.log10(data2d).nan_to_num(nan=0., neginf=0.) # incase 0 in data, cause log(0) output
            colorbar_title = 'log value'
        else:
            colorbar_title = None
        self.add_trace(go.Heatmap(
            z=data2d.T,
            colorscale=colorscale,
            colorbar={'title': colorbar_title}
            ))
        self.update_xaxes(
            scaleanchor='y',
            scaleratio=1,
            constrain='domain'
            )
    
    @staticmethod
    def __surfacecolor(coord: Tensor, value: Tensor|float|int|None, log_value: bool = True) -> Tensor:
        value = 1 if value is None else value
        if isinstance(value, (float, int)):
            surfacecolor = torch.full_like(coord, value)
        else:
            if log_value:
                surfacecolor = torch.log10(value).nan_to_num(nan=0., neginf=0.) # incase 0 in data, cause log(0) output
            else:
                surfacecolor = value
        return surfacecolor
    
    def plot_surface3d(self, x: Tensor, y: Tensor, z: Tensor, value: Optional[Tensor|float|int] = None, log_value: bool = True, colorscale: Optional[str] = None, **kwargs) -> None:
        x, y, z, value = self.__ensure_cpu_tensor(x, y, z, value)
        surfacecolor = self.__surfacecolor(x, value, log_value)
        self.add_trace(go.Surface(
            x=x, y=y, z=z, surfacecolor=surfacecolor, coloraxis='coloraxis', **kwargs
        ))
        self.update_layout(coloraxis = {'colorscale': colorscale})
        self.update_layout(scene_aspectmode='data') # make equal aspect, or use fig.update_scenes(aspectmode='data')        
        
    
    def plot_volume3d(self, x: Tensor, y: Tensor, z: Tensor, value: Tensor, log_value: bool = False, opacity: float = 0.1, surface_count: int = 21, colorscale: Optional[str] = None, **kwargs) -> None:
        x, y, z, value = self.__ensure_cpu_tensor(x, y, z, value)
        if log_value:
            value = torch.log10(value).nan_to_num(nan=0., neginf=0.) # incase 0 in data, cause log(0) output
            colorbar_title = 'log value'
        else:
            colorbar_title = None
        self.add_trace(go.Volume(
            x=x.flatten(),
            y=y.flatten(),
            z=z.flatten(),
            value=value.flatten(),
            opacity=opacity,
            surface_count=surface_count,
            coloraxis='coloraxis',
            colorbar={'title': colorbar_title},
            **kwargs
        ))
        self.update_layout(scene_aspectmode='data') # make equal aspect
        self.update_layout(coloraxis={'colorscale': colorscale})
        
    def plot_voxel3d(self, x: Tensor, y: Tensor, z: Tensor, spacing: float, name: Optional[str] = None, showlegend: bool = True, **kwargs) -> None:
        x, y, z = self.__ensure_cpu_tensor(x, y, z)
        self.add_trace(Voxel(
            xc=x,
            yc=y,
            zc=z,
            spacing=spacing,
            name=name,
            showlegend=showlegend,
            **kwargs
        ))
        self.update_layout(scene_aspectmode='data') # make equal aspect
        
    
    def plot_detector(self, x: Tensor, y: Tensor, z: Tensor, value: Optional[Tensor] = None, log_value: bool = True, colorscale: Optional[str] = None) -> None:
        x, y, z, value = self.__ensure_cpu_tensor(x, y, z, value)
        self.plot_surface3d(x, y, z, value=value, log_value=log_value, colorscale=colorscale)
        
        # plot origin
        self.add_scatter3d(x=[0,], y=[0,], z=[0,], mode='markers', showlegend=False)
        
        # plot direct beam in y axis direction
        self.add_scatter3d(x=[0,0], y=[0,y.max().item()], z=[0,0], mode='lines', showlegend=False)
        
        # plot light edges on detector
        v0 = torch.tensor([0., 0., 0.])
        v1 = torch.tensor((x[0,0], y[0,0], z[0,0]))
        v2 = torch.tensor((x[0,-1], y[0,-1], z[0,-1]))
        v3 = torch.tensor((x[-1,-1], y[-1,-1], z[-1,-1]))
        v4 = torch.tensor((x[-1,0], y[-1,0], z[-1,0]))
        ex, ey, ez = torch.unbind(
            torch.stack([v0,v1,v2,v3,v4], dim=1),
            dim=0
            )
        self.add_mesh3d(
            x=ex,
            y=ey,
            z=ez,
            alphahull=0,
            color='gray',
            opacity=0.1,
        )
        self.update_layout(scene_aspectmode='data')
