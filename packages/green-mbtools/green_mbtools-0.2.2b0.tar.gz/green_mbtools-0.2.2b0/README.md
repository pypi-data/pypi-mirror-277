[![GitHub license](https://img.shields.io/github/license/Green-Phys/green-mbpt?cacheSeconds=3600&color=informational&label=License)](./LICENSE)

```

 █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀▄
 █ ▄▄ █▄▄▀ █▀▀ █▀▀ █  █
 █▄▄█ ▀ ▀▀ ▀▀▀ ▀▀▀ ▀  ▀

 █▀▄▀█ █▀▀█ █▀▀▄ █  █     █▀▀█ █▀▀█ █▀▀▄ █  █ 　 ▀▀█▀▀ █▀▀█ █▀▀█ █   █▀▀
 █ █ █ █▄▄█ █  █ █▄▄█ ▀▀  █▀▀▄ █  █ █  █ █▄▄█ 　   █   █  █ █  █ █   ▀▀█
 █   █ ▀  ▀ ▀  ▀ ▄▄▄█     █▄▄█ ▀▀▀▀ ▀▀▀  ▄▄▄█ 　   █   ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀

***

`Green/MBTools` is a collection of tools used to generate initial data and perform post-processing routines for `Green` software package

## Installation

### Dependencies
  - `numpy` version > 1.0
  - `h5py` version > 3.0.0
  - `PySCF` version >= 2.0
  - `numba` version >= 0.57

### Installation

```ShellSession
$ pip install green-mbtools
```

## Basic usage

```Python
import green_mbtools as mb
from pyscf.pbc import scf


# Define system geometry
a = '''0.0,  2.7155, 2.7155
2.7155, 0.0,  2.7155
2.7155, 2.7155, 0.0'''

atoms = 'H 0.0  0.0  0.0; H 1.35775 1.35775 1.35775'

# Setup simulation parameters
params = {'a' : a, 'atom': atoms, 'basis': "sto3g", 'nk': 2, 'ns' : 2,
          'mean_field': scf.KUHF, 'output_path' : 'init.h5', 'df_int': 1 }
args = mb.Namespace(params)

# Solve mean-field initial solution
pp = mb.pyscf_init(args)
pp.mean_field_input()

```


This work is supported by the National Science Foundation under the award OAC-2310582
