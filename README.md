# trimesh_upstream
[![Build Status](https://travis-ci.org/geometries/trimesh_upstream.svg?branch=master)](https://travis-ci.org/geometries/trimesh_upstream)

A project to check and see if a fresh installation of trimesh with `pip install trimesh[all]` works on all major platforms without having to use any package manager other than pip (conda, apt, etc).

In an ideal world, all upstream packages would have wheels which include all necessary shared libraries for Python 2.7, 3.4-3.6 on OSX, Windows, and Manylinux.

The goal of this is to set up failing packages with a `cibuildwheel` build configuration and then PR to the original project, or fork and set up a new PyPi deployment that `trimesh` can require.

## Current Status

Package | Status | Details
--------|--------|---------
`numpy` | :heavy_check_mark: | great wheel support
`scipy` | :heavy_check_mark: | great wheel support
`lxml` | :heavy_check_mark: | great wheel support
`pyglet` | :heavy_check_mark: | pure Python 2/3
`svg.path` | :heavy_check_mark: | pure Python 2/3
`colorlog` | :heavy_check_mark: | pure Python 2/3
`sympy` | :heavy_check_mark: | seems to work generally
`msgpack` | :heavy_check_mark: | Manylinux and Windows wheels
`python-fcl` | :heavy_exclamation_mark: | Manylinux wheels, no Windows or OSX
`rtree` | :x: | wheels require `libspatialindex` (not bundled)
`shapely` | :x: | wheels require `libgeos` (not bundled)
`triangle` | :x: | requires compilation, but usually works
