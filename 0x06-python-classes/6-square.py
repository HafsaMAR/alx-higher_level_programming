#!/usr/bin/python3

"""This module defines a class Square"""


class Square:
    """  A class that Create the private instance attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size of the square"""
        self.__size = size
        self.postion = position

    @property
    def size(self):
        """Public instance method that returns the current square size"""

        return self.__size

    def postion(self):

        return self.__postion

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def postion(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not (isinstance(y, int)) \
                or x < 0 or y < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__postion = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print()
        x, y = self.postion
        for _ in range(self.size):
            print(' ' * x)
            print("#" * self.size)
        for _ in range(y):
            print()
