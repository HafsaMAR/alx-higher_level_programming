#!/usr/bin/python3
"""Unitest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    def test_max_integer_None(self):
        # test if the list is empty
        self.assertEqual(max_integer([]), None)
        

if __name__ == '__main__':
    unittest.main()