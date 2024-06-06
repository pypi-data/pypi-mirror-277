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

### Build and Install

```ShellSession
$ git clone https://github.com/Green-Phys/green-mbpt
$ cd green-mbpt
$ mkdir build && cd build
$ cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/path/to/weakcoupling/install/dir ..
$ make
$ make test
$ make install
```

## Basic usage




This work is supported by the National Science Foundation under the award OAC-2310582
