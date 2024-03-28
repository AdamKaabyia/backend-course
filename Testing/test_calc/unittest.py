import unittest

from ..basic4 import *


class TestCalculator(unittest.TestCase):
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            add_sub_div_mul(10, 0, '/')

    def test_unsupported_operation(self):
        with self.assertRaises(ValueError):
            #add_sub_div_mul('5', 5, '+')
            add_sub_div_mul(10, 5, '%')

    def test_add(self):
        self.assertEqual(add_sub_div_mul(2, 3, '+'), 5)

    def test_subtract(self):
        self.assertEqual(add_sub_div_mul(5, 2, '-'), 3)

    def test_divide(self):
        self.assertEqual(add_sub_div_mul(6, 2, '/'), 3)

    def test_multiply(self):
        self.assertEqual(add_sub_div_mul(3, 4, '*'), 12)


if __name__ == '__main__':
    unittest.main()
