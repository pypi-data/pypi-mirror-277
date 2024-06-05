from pathlib import Path
from typing import Optional
from tempfile import NamedTemporaryFile

import torch
import panel as pn
pn.extension("plotly")

from ..readfile import read_math, read_pdb, read_stl
from ..model import GridModel
from ..plot import Figure


read_funcs = {'.py': read_math, '.stl': read_stl, '.pdb': read_pdb}
model: Optional[GridModel] = None


# read file
file_input         = pn.widgets.FileInput(accept='.stl,.pdb,.py')
n_long             = pn.widgets.IntInput(name='Number of points on longest edge', value=50)
spacing            = pn.widgets.FloatInput(name='Spacing between points (overide above)', value=0, start=0, end=None)
other_read_args    = pn.widgets.TextInput(name='Other args of model input', placeholder='format: R=10,probe=\"neutron\"')
read_file_button   = pn.widgets.Button(name='Read file')
plot_type          = pn.widgets.Select(name='Model plot type', options=['Voxel', 'Volume'], value='Voxel')
plot_model_button  = pn.widgets.Button(name='Plot model')
qmin               = pn.widgets.FloatInput(name='Q min', value=0.001)
qmax               = pn.widgets.FloatInput(name='Q max', value=1.0)
qnum               = pn.widgets.IntInput(name='Number of Q points', value=200)
offset             = pn.widgets.IntInput(name='Intensity average offset', value=1000)
calc_curve_button  = pn.widgets.Button(name='Calculate SAS curve')

def read_file(button, n_long, spacing, other_read_args):
    if button:
        global file_input, model
        suffix = Path(file_input.filename).suffix.lower()
        with NamedTemporaryFile(mode='wb', suffix=suffix, delete=False) as tmpf:
            tempfilename = tmpf.name
            tmpf.write(file_input.value)
        # print(model)
        kwargs = eval(f'dict({other_read_args})')
        spacing = None if spacing == 0. else spacing
        print(spacing, kwargs)
        model = read_funcs[suffix](tempfilename, n_long=n_long, spacing=spacing, **kwargs)
        Path(tempfilename).unlink()
        
def plot_model(button, plot_type):
    global model
    if button and model is not None:
        fig = Figure()
        x, y, z = model.real_grid.coord3d
        sld = model.sld
        if plot_type.lower() == 'voxel':
            fig.plot_voxel3d(x[sld!=0], y[sld!=0], z[sld!=0], model.real_grid.spacing, showlegend=False)
        elif plot_type.lower() == 'volume':
            fig.plot_volume3d(x, y, z, sld, showlegend=False)
        return pn.pane.Plotly(fig, width=700, height=500)
    
def calc_sas_curve(button, qmin, qmax, qnum, offset):
    if button and model is not None:
        model.scatter()
        q = torch.linspace(qmin, qmax, qnum)
        I = model.intensity_ave(q, offset=offset)
        fig = Figure()
        fig.plot_curve1d(q, I)
        return pn.pane.Plotly(fig, width=700, height=500)

def app():
    _app = pn.Row(
        pn.Column(
            # 'Upload model file',
            file_input         ,
            n_long             ,
            spacing            ,
            other_read_args    ,
            read_file_button   ,
            plot_type          ,
            plot_model_button  ,
            qmin               ,
            qmax               ,
            qnum               ,
            offset             ,
            calc_curve_button  ,
            pn.bind(read_file, read_file_button, n_long, spacing, other_read_args),
        ),
        pn.Column(
            pn.bind(plot_model, plot_model_button, plot_type),
            pn.bind(calc_sas_curve, calc_curve_button, qmin, qmax, qnum, offset),
        ),
    )
    _app.servable()
    return _app
