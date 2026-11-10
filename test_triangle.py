import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_normal_area(self):
        self.assertEqual(area(4, 5), 10.0)
        
    def test_normal_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)