#!/usr/bin/python3

"""This module defines a class Square"""


class Square:
    """  A class that Create the private instance attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size of the square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position.

        Args:
        value (tuple): position of the square.

        Raise:
            TypeError: if value is not a tuple of positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not (isinstance(y, int)) \
                or x < 0 or y < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Public instance method that prints in stdout the square using #,
        while printing spaces fir the position of the square
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print("\n")
            for _ in range(self.size):
                print(' ' * self.position[0] + "#" * self.size)
