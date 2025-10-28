import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    # Right triangles (order-insensitive)
    def test_right_345(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
    def test_right_perm(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    # Equilateral
    def test_equilateral_small(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')
    def test_equilateral_medium(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral')

    # Isosceles (valid)
    def test_isosceles_a(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles')
    def test_isosceles_b(self):
        self.assertEqual(classifyTriangle(8, 5, 5), 'Isosceles')

    # Scalene (valid, not right)
    def test_scalene_a(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene')
    def test_scalene_b(self):
        self.assertEqual(classifyTriangle(4, 6, 9), 'Scalene')

    # Not a triangle (triangle inequality)
    def test_not_triangle_sum_eq(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')
    def test_not_triangle_sum_lt(self):
        self.assertEqual(classifyTriangle(2, 3, 6), 'NotATriangle')

    # Invalid inputs
    def test_invalid_zero(self):
        self.assertEqual(classifyTriangle(0, 5, 5), 'InvalidInput')
    def test_invalid_negative(self):
        self.assertEqual(classifyTriangle(-1, 5, 5), 'InvalidInput')
    def test_invalid_type(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')
    def test_invalid_too_large(self):
        self.assertEqual(classifyTriangle(201, 10, 10), 'InvalidInput')

if __name__ == '__main__':
    unittest.main()