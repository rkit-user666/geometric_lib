import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    
    def test_zero_mul(self):
        """Тест: умножение на ноль должно давать ноль"""
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        """Тест: вычисление площади квадрата 10х10"""
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_normal_area(self):
        """Тест: стандартные значения сторон"""
        res = area(4, 5)
        self.assertEqual(res, 20)

    def test_zero_perimeter(self):
        """Тест: периметр со стороной 0"""
        res = perimeter(5, 0)
        self.assertEqual(res, 10)

    def test_normal_perimeter(self):
        """Тест: стандартный периметр"""
        res = perimeter(3, 7)
        self.assertEqual(res, 20)