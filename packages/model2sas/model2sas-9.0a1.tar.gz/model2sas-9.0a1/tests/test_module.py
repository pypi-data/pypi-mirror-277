import math
import torch
from torch import Tensor

import model2sas
import model2sas.calcfunc

model2sas.global_vars.DEFAULT_DEVICE = 'cpu'



def logscale_close(t1: Tensor, t2: Tensor) -> bool:
    notnan = lambda t: t[~t.isnan()]
    num_notnan = lambda t: notnan(t).numel()
    ave = lambda t: t.nanmean()
    sigma = lambda t: torch.sqrt( ((t-ave(t))**2).nansum() / (num_notnan(t)-1) )
    dev = lambda t: t-ave(t)
    def del_outliers(t, nsigma=3):
        sum_n_outlier = 0
        outlier = dev(t).abs() > nsigma*sigma(t)
        while outlier.sum().item() > 0:
            sum_n_outlier += outlier.sum().item()
            if sum_n_outlier > 0.1*t.numel():
                raise RuntimeError('Too many outliers')
            t = torch.where(outlier, torch.nan, t)
            outlier = dev(t).abs() > nsigma*sigma(t)
        # print(sum_n_outlier)
        return t
    
    logoffset = torch.log10(t1) - torch.log10(t2)
    logoffset = del_outliers(logoffset)
    return (sigma(logoffset)/ave(logoffset) < 0.001).item()


def F1d_sph(q1d: Tensor, R: float, sld: float = 1):
    u = q1d*R
    return (4*torch.pi*R**3)/3 * sld * (3/u**3) * (torch.sin(u) - u*torch.cos(u))

def I1d_sphere(q1d: Tensor, R: float, sld: float = 1) -> Tensor:
    return (F1d_sph(q1d, R, sld))**2

def I1d_core_shell_sphere(q1d: Tensor, R_core: float, thickness: float, sld_core: float, sld_shell: float) -> Tensor:
    return (F1d_sph(q1d, R_core, sld_core) + F1d_sph(q1d, R_core+thickness, sld_shell) - F1d_sph(q1d, R_core, sld_shell))**2


def core_shell_sphere_model(R_core, thickness, sld_core, sld_shell) -> model2sas.GridModel:
    b1, b2 = [-(R_core+thickness)]*3, [R_core+thickness]*3
    bbox = model2sas.model.BoundingBox(*b1, *b2)
    x1d, y1d, z1d, x, y, z = model2sas.readfile.meshgrid(bbox)
    sld = torch.zeros_like(x)
    r, theta, phi = model2sas.calcfunc.convert_coord(x, y, z, 'car', 'sph')
    sld[r<=R_core] = sld_core
    sld[(r>=R_core) & (r<=R_core+thickness)] = sld_shell
    model = model2sas.GridModel(x1d, y1d, z1d, sld)
    model.scatter()
    return model


def test_gridmodel():
    # geo parameters
    R_core, thickness, sld_core, sld_shell = 10, 5, -2, 1
    model = core_shell_sphere_model(R_core, thickness, sld_core, sld_shell)
    model.translate(32, 57, 101)
    model.rotate((-2.1, 1.5, 10.4), 0.41*torch.pi)
    
    q = torch.linspace(0.01, 2, steps=1000)
    I = model.intensity_ave(q)
    
    # theoretical
    Itheo = I1d_core_shell_sphere(q, R_core, thickness, sld_core, sld_shell)
    
    fig = model2sas.Figure()
    fig.plot_curve1d(q, Itheo, name='theoretical')
    fig.plot_curve1d(q, I, name='model2sas')
    fig.show()
    
    assert logscale_close(I, Itheo), 'Model2SAS calculated inconsistent with theoretical result'
    
    
def test_assemblymodel_and_transform():
    
    R, H, sld_value1, sld_value2 = 10, 30, -1, 1.5

    jcyl = model2sas.read_math('./tests/modelfiles/joined_cylinder.py', R=R, H=H, sld_value1=sld_value1, sld_value2=sld_value2)
    jcyl.scatter()
    
    d = 5*H
    cyl1 = model2sas.read_math('./tests/modelfiles/cylinder.py', R=R, H=H/2, sld_value=sld_value1)
    cyl1.scatter()
    cyl1.translate(0, 0, -d)
    cyl1.rotate((0, 3, 0), torch.pi/4)
    
    cyl2 = model2sas.read_math('./tests/modelfiles/cylinder.py', R=R, H=H/2, sld_value=sld_value2)
    cyl2.scatter()
    cyl2.rotate((0, -0.7, 0), -torch.pi/4)
    sqrt2 = math.sqrt(2)
    cyl2.translate(-d/sqrt2, 0, -d/sqrt2)
    cyl2.translate(H/2/sqrt2, 0, H/2/sqrt2)
    
    assm = model2sas.AssemblyModel(cyl1, cyl2)

    q = torch.linspace(0.001, 2, 500)
    Ij = jcyl.intensity_ave(q)
    Ia = assm.intensity_ave(q)
    
    fig = model2sas.Figure()
    fig.plot_curve1d(q, Ij, name='single')
    fig.plot_curve1d(q, Ia, name='2 assembled')
    fig.show()
    
    assert logscale_close(Ij, Ia)



def test_readfile():
    
    def normal_flow(model):
        model.scatter()
        model.translate(32, 57, 101)
        model.rotate((-2.1, 1.5, 10.4), 0.41*torch.pi)
        q = torch.linspace(0.01, 2, steps=1000)
        model.intensity_ave(q)
    
    model = model2sas.readfile.read_stl('./tests/modelfiles/torus.stl', centering=True)
    normal_flow(model)
    
    model = model2sas.readfile.read_pdb('./tests/modelfiles/3v03.pdb')
    normal_flow(model)
    model = model2sas.readfile.read_pdb('./tests/modelfiles/3v03.pdb', probe='neutron')
    normal_flow(model)
    
    model = model2sas.readfile.read_math('./tests/modelfiles/core_shell_sphere.py', R_core=20, thickness=30, sld_core=2, sld_shell=-1)
    normal_flow(model)
    
    MathModelClass = model2sas.readfile.import_mathmodel_class('./tests/modelfiles/core_shell_sphere.py')
    mathmodel = MathModelClass()
    model = model2sas.readfile.read_math(mathmodel, R_core=20, thickness=30, sld_core=2, sld_shell=-1)
    normal_flow(model)
    

def test_plot():
    R_core, thickness, sld_core, sld_shell = 10, 5, -2, 1
    model = core_shell_sphere_model(R_core, thickness, sld_core, sld_shell)
    x, y, z = model.real_grid.coord3d
    sld = model.sld

    fig = model2sas.Figure()
    fig.plot_volume3d(x, y, z, sld)
    fig.show()
    
    fig = model2sas.Figure()
    fig.plot_voxel3d(x[sld!=0], y[sld!=0], z[sld!=0], model.real_grid.spacing)
    fig.show()
    
    fig = model2sas.Figure()
    q = torch.linspace(0.01, 2, steps=1000)
    I = model.intensity_ave(q)
    fig.plot_curve1d(q, I)
    fig.show()
    
    fig = model2sas.Figure()
    q1d = torch.linspace(-1, 1, 50)
    qx, qy, qz = torch.meshgrid(q1d, q1d, q1d, indexing='ij')
    I = model.intensity(qx, qy, qz)
    fig.plot_volume3d(qx, qy, qz, I)
    fig.show()
    
    fig = model2sas.Figure()
    fig.plot_surface2d(I[:,:,0])
    fig.show()


if __name__ == '__main__':
    test_gridmodel()
    test_assemblymodel_and_transform()
    test_readfile()
    test_plot()
    