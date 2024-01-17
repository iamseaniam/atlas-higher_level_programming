#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3, 4])

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            max_integer("")
            
    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 500000, 2000000]), 2000000)

if __name__ == '__main__':
    unittest.main()
