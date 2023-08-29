#!/usr/bin/python3

"""This module defines a class Square"""

class Square:
    """  A class that Create the private instance attribute size"""

    def __init__(self, size=0):
        """Initialize the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
