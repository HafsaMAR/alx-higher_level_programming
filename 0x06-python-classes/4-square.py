#!/usr/bin/python3

"""This module defines a class Square"""


class Square:
    """  A class that Create the private instance attribute size"""

    def __init__(self, size=0):
        """Initialize the size of the square"""
        self.__size = size

    @property
    def size(self):
        """Public instance method that returns the current square size"""

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2
