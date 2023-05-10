import unittest

from accounts.utils import mul, sum, sub, div


class TestMathFunctions(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(0, 5), 0)
        self.assertEqual(mul(-2, -3), 6)

    def test_sum(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(0, 5), 5)
        self.assertEqual(sum(-2, -3), -5)

    def test_sub(self):
        self.assertEqual(sub(2, 3), -2)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-2, -3), 1)

    def test_div(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(1, 3), 0.3333333333333333)