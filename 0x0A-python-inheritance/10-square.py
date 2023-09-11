#!/usr/bin/python3

"""Module for the class square inheriting the Rectangle class attributes"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """Initialize the square attributes
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of the square
        Returns:
            area of the square
        """
        return self.__size**2
