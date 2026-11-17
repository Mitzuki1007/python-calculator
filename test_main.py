"""Автоматические тесты калькулятора на unittest."""

import unittest

from main import add, subtract, multiply, divide, average


class CalculatorTests(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(9, 4), 5)

    def test_multiply_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_average_numbers(self):
        self.assertEqual(average([2, 4, 6]), 4)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_average_empty_list_raises_error(self):
        with self.assertRaises(ValueError):
            average([])

    def test_average_single_number(self):
        self.assertEqual(average([7]), 7)


if __name__ == "__main__":
    unittest.main()
