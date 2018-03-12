# trimesh_upstream
[![Build Status](https://travis-ci.org/geometries/trimesh_upstream.svg?branch=master)](https://travis-ci.org/geometries/trimesh_upstream)

A project to check and see if a fresh installation of trimesh with `pip install trimesh[all]` works on all major platforms without having to use any package manager other than pip (conda, apt, etc).

In an ideal world, all upstream packages would have wheels for Python 2.7, 3.4-3.6 on OSX, Windows, and Manylinux.

The goal of this is to set up failing packages with a `cibuildwheel` build configuration and then PR to the original project, or fork and set up a new PyPi deployment that `trimesh` can require.

## Current Status
- `numpy`: :white_check_mark: great wheel support
- `scipy`: :white_check_mark: great wheel support
- `lxml`: :white_check_mark: great wheel support
- `pyglet`: :white_check_mark: pure Python 2/3
- `svg.path`: :white_check_mark: pure Python 2/3
- `colorlog`: :white_check_mark: pure Python 2/3
- `python-fcl`: :exclamation_mark: Manylinux wheels, no Windows or OSX
- `msgpack`: :exclamation_mark: ManyLinux wheels
- `rtree`: :x: wheels require `libspatialindex` (not bundled)
- `shapely` :x: wheels require `libgeos` (not bundled)
- `meshpy` :x: :x: requires compilation; fails often
- `sympy`: :question: depends on `mpmath`, but seems to work generally
