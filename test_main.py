"""Автоматические тесты калькулятора на unittest."""

import unittest

from main import (
    addition,
    subtraction,
    multiplication,
    division,
    arithmetic_mean
)


class CalculatorTests(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(addition(2, 3), 5)

    def test_subtract_numbers(self):
        self.assertEqual(subtraction(9, 4), 5)

    def test_multiply_numbers(self):
        self.assertEqual(multiplication(3, 4), 12)

    def test_divide_numbers(self):
        self.assertEqual(division(10, 2), 5)

    def test_average_numbers(self):
        self.assertEqual(arithmetic_mean([2, 4, 6]), 4)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    def test_average_empty_list_raises_error(self):
        with self.assertRaises(ValueError):
            arithmetic_mean([])

    def test_average_single_number(self):
        self.assertEqual(arithmetic_mean([7]), 7)


if __name__ == "__main__":
    unittest.main()