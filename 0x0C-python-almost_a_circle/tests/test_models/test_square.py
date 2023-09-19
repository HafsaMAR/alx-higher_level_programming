#!/usr/bin/python3

"""Test module for the class Square"""

import unittest

from models.square import Square


class test_square(unittest.TestCase):
    """Test the Square class imported from models.square module"""
    
    def test_attributes(self):
        """Testing attributes"""
        obj = Square(1)
        self.assertEqual(obj.size, 1)
        obj = Square(1, 2)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        obj = Square(1, 2, 3)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)
        obj = Square(1, 2, 3, 4)
        self.assertEqual(obj.id, 4)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    
    def test_attributes_validation(self):
        """Testing attributes validation"""

        """---WIDTH---"""

        with self.assertRaises(TypeError) as traceback:
            S = Square("a")
        self.assertEqual(str(traceback.exception), "width must be an integer")
        with self.assertRaises(ValueError) as traceback:
            S = Square(-1)
        self.assertEqual(str(traceback.exception), "width must be > 0")

        """---X---"""

        with self.assertRaises(TypeError) as traceback:
            S = Square(1, "a")
        self.assertEqual(str(traceback.exception), "x must be an integer")
        with self.assertRaises(ValueError) as traceback:
            S = Square(1, -1)
        self.assertEqual(str(traceback.exception), "x must be >= 0")

        """---Y---"""
        with self.assertRaises(TypeError) as traceback:
            S = Square(1, 2, "a")
        self.assertEqual(str(traceback.exception), "y must be an integer")
        with self.assertRaises(ValueError) as traceback:
            S = Square(1, 2, -1)
        self.assertEqual(str(traceback.exception), "y must be >= 0")