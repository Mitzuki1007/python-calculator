"""Автоматические тесты калькулятора на unittest."""

import unittest
from io import StringIO
from unittest.mock import patch

from main import (
    addition,
    subtraction,
    multiplication,
    division,
    arithmetic_mean,
    show_help,
    main
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

    def test_show_help_displays_information(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            show_help()

        help_text = output.getvalue()

        self.assertIn("1. Сложение", help_text)
        self.assertIn("5. Среднее арифметическое", help_text)
        self.assertIn("6. Помощь", help_text)
        self.assertIn("0. Выход", help_text)

    def test_invalid_menu_choice_displays_error(self):
        with patch("builtins.input", side_effect=["9", "0"]):
            with patch("sys.stdout", new_callable=StringIO) as output:
                main()

        result = output.getvalue()

        self.assertIn(
            "Ошибка: такого пункта меню нет.",
            result
        )


if __name__ == "__main__":
    unittest.main()