import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area(0), 0)
        
    def test_normal_area(self):
        self.assertEqual(area(5), 25)
        
    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)
        
    def test_normal_perimeter(self):
        self.assertEqual(perimeter(5), 20)