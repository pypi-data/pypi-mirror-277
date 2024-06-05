# import click
from pathlib import Path
import math
import time

import rich_click as click
import torch
import numpy as np

from ..readfile import read_math, read_pdb, read_stl
from ..model import GridModel
from ..plot import Figure
from .. import global_vars
global_vars.PRINT_LOG = False

read_funcs = {'.py': read_math, '.stl': read_stl, '.pdb': read_pdb}

@click.command()
@click.option("--output", '-o', default=None, type=str, help="Output file, default is the stem of FILE with .dat suffix")
@click.option("--nlong", default=50, type=int, help="Number of sampling points on longest edge of bounding box")
@click.option("--spacing", default=None, type=float, help="Spacing iof sampling meshgrid. Override nlong argument")
# @click.option("--nreciprocal", default=0, type=int, help="")
@click.option("--qmin", default=0.01, type=float, help="Minimum value of scattering vector to be simulated")
@click.option("--qmax", default=1.0, type=float, help="Maximum value of scattering vector to be simulated")
@click.option("--qnum", default=100, type=int, help="Number of scattering vector points")
@click.option("--logq", is_flag=True, help="Whether scattering vector values are logged distributed")
@click.option("--offset", default=1000, type=int, help="Offset in orientation average")
@click.argument('file')
def run(output, nlong, spacing, qmin, qmax, qnum, logq, offset, file):
    """Program to simulate small angle scattering curve from 3D model.
    """
    # print(output, nlong, spacing, offset, qmin, qmax, qnum, logq, file)
    suffix = Path(file).suffix.lower()
    read_func = read_funcs[suffix]
    if logq:
        q = torch.logspace(math.log10(qmin), math.log10(qmax), qnum, base=10)
    else:
        q = torch.linspace(qmin, qmax, qnum)
    if output is None:
        output = Path(file).with_suffix('.dat')
    
    t0 = time.perf_counter()
    model = read_func(file, n_long=nlong, spacing=spacing)
    model.scatter()
    I = model.intensity_ave(q, offset=offset)
    t1 = time.perf_counter()
    
    np.savetxt(
        output,
        np.stack([q.numpy(), I.numpy()], axis=1),
        delimiter='\t',
        header='Simulated SAS curve by Model2SAS\nq\tI',
    )
    print(f'Simulation completed in {t1-t0:.3f} sec, data stored in {output}')

if __name__ == '__main__':
    run()