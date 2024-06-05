# Model2SAS

![GitHub Actions Workflow Status](https://github.com/molybd/Model2SAS/actions/workflows/python-package.yml/badge.svg)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/molybd/Model2SAS/dev)
![GitHub License](https://img.shields.io/github/license/molybd/Model2SAS)
![Static Badge](https://img.shields.io/badge/doi-10.1107%2FS1600576722003600-yellow?logo=doi&logoSize=auto&link=https%3A%2F%2Fjournals.iucr.org%2Fpaper%3FS1600576722003600)

Program to simulate small angle scattering curve from 3D models. Models can be 3D shape stored in .stl file, protein structure in .pdb file and math description in .py file. Module, CLI and GUI are all prepared for convenience.

If you use Model2SAS in your research, please cite: 

*Li, Mu, and Yin, Panchao, Model2SAS: software for small-angle scattering data calculation from custom shapes., J. Appl. Cryst., 2022, 55, 663-668.* 
https://doi.org/10.1107/S1600576722003600

## Installation

```shell
pip install model2sas
```

Or install with latest source code:

```shell
git clone git@github.com:molybd/Model2SAS.git
cd Model2SAS
pip install .
```

or download the source code zip file and `pip install .`

GPU computation may not be available with automatically installed dependencies. If you have GPUs available for PyTorch, you can uninstall pytorch first with `pip uninstall torch` and then reinstall with instructions as https://pytorch.org/ or elsewhere.

## Usage

### Module

First import model file with file reader functions `read_stl`, `read_pdb`, `read_math`:

```python
import model2sas
model = model2sas.read_stl('resources/models/torus.stl')
```

All the model files read will generate same type`GridModel`. You can control the precision of grid model by setting key word arguments either `n_long` or `spacing` (`spacing` will override `n_long`). If pytorch are configured with GPU, you can also set `device` key word argument like `device="cuda"`, device names will be used in pytorch.

There are unique key word arguments for different types of model, e.g. for .pdb model, you can set `probe="xray"` or  `probe="neutron"`  and `wavelength` to simulate SAXS or SANS of proteins; for .py math model, you can set parameters of the specific model. Examples:

```python
model = model2sas.read_pdb('resources/models/3v03.pdb', spacing=1, probe='xray', wavelength=1.24) # points spacing 1 angstrom, SAXS with 10keV X-ray
model = model2sas.read_math('resources/models/cylinder.pdb', R=20, H=50) # cylinder with 20 radius and 50 height
```

After read model file, do scattering on `model`, and measure the orientation averaged intensities on given q values:

```python
import torch
model.scatter()
q = torch.linspace(0.01, 1, 200) # 200 evenly spaced q values from 0.01 to 1
I = model.intensity_ave(q)
```

That's all! Just this simple.

Detailed descriptions on each arguments will be given in docstring.

### CLI

Use with command `model2sas`, type `model2sas --help` for instructions.

```shell
> model2sas --help

 Usage: model2sas [OPTIONS] FILE

 Program to simulate small angle scattering curve from 3D model.

╭─ Options ───────────────────────────────────────────────────────────────────────────╮
│ --output   -o  TEXT     Output file, default is the stem of FILE with .dat suffix   │
│ --nlong        INTEGER  Number of sampling points on longest edge of bounding box   │
│ --spacing      FLOAT    Spacing iof sampling meshgrid. Override nlong argument      │
│ --qmin         FLOAT    Minimum value of scattering vector to be simulated          │
│ --qmax         FLOAT    Maximum value of scattering vector to be simulated          │
│ --qnum         INTEGER  Number of scattering vector points                          │
│ --logq                  Whether scattering vector values are logged distributed     │
│ --offset       INTEGER  Offset in orientation average                               │
│ --help                  Show this message and exit.                                 │
╰─────────────────────────────────────────────────────────────────────────────────────╯

```

### GUI

WebUI is provided with command `model2sas-gui`. UI is intuitive and similar logic with module and CLI, should be easy to get started quickly.

## Additional notes 

Based on the basic theory of small-angle scattering, there are no essential difference between X-ray scattering and neutron scattering. So here the values are just scattering length density (SLD). It's up to users that the SLDs are X-ray SLD or neutron SLD. As for the unit, there is no assumed unit except for pdb mdoel, it's also up to users. The output q unit is just the reverse of model unit assumed by user. For pdb model, it's angstrom and reverse angstrom.
