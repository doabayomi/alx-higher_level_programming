#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 3, 2, 5, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-4, -33, -2, -9, -4])
        self.assertEqual(result, -2)

    def test_mixed_numbers(self):
        result = max_integer([-2, 2, -4, 5, 0])
        self.assertEqual(result, 5)

    def test_single_number(self):
        result = max_integer([22])
        self.assertEqual(result, 22)

    def test_repetition(self):
        result = max_integer([4, 4, 4, 4])
        self.assertEqual(result, 4)

    def test_float(self):
        result = max_integer([2.5, 2.2, 3.6])
        self.assertEqual(result, 3.6)

    def test_empty_list(self):
        result = max_integer()
        self.assertIsNone(result)
    
    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
