import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(0), 0)
        
    def test_normal_area(self):
        self.assertAlmostEqual(area(3), math.pi * 9)
        
    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)
        
    def test_normal_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)