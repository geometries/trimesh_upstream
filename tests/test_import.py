import unittest

import trimesh
import rtree
import numpy as np
from shapely.geometry import Point, Polygon
from scipy import spatial


class TestBasic(unittest.TestCase):
    def test_path(self):
        a = np.array(Point([0,0]).buffer(1.0).exterior.coords)
        b = trimesh.load_path(a)

        assert trimesh.util.is_shape(b.vertices, (-1,2))
        
    def test_prim(self):
        a = trimesh.primitives.Sphere()
        
        assert a.volume > 1.0
        assert len(a.identifier_md5) > 0
        assert trimesh.util.is_shape(a.vertices, (-1,3))

if __name__ == '__main__':
    unittest.main()
