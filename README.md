# trimesh_upstream
[![Build Status](https://travis-ci.org/geometries/trimesh_upstream.svg?branch=master)](https://travis-ci.org/geometries/trimesh_upstream)

A project to check and see if a fresh installation of trimesh with `pip install trimesh[all]` works on all major platforms without having to use any package manager other than pip (conda, apt, etc).

In an ideal world, all upstream packages would have wheels which include all necessary shared libraries for Python 2.7, 3.4-3.6 on OSX, Windows, and Manylinux.

The goal of this is to set up failing packages with a `cibuildwheel` build configuration and then PR to the original project, or fork and set up a new PyPi deployment that `trimesh` can require.

## Current Status

Package | Status | Details
--------|--------|---------
`numpy` | :check_mark: | great wheel support
`scipy` | :check_mark: | great wheel support
`lxml` | :check_mark: | great wheel support
`pyglet` | :check_mark: | pure Python 2/3
`svg.path` | :check_mark: | pure Python 2/3
`colorlog` | :check_mark: | pure Python 2/3
`sympy` | :check_mark: | seems to work generally
`msgpack` | :check_mark: | Manylinux and Windows wheels
`python-fcl` | :heavy_exclamation_mark: | Manylinux wheels, no Windows or OSX
`rtree` | :x: | wheels require `libspatialindex` (not bundled)
`shapely` | :x: | wheels require `libgeos` (not bundled)
`triangle` | :x: | requires compilation, but usually works
