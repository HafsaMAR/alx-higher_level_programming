#!/usr/bin/python3

"""Module for rectange class that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from baseGeometry superclass
    """
    def __init__(self, width, height):
        """
        Initialize an instance of the rectangle class

        Args:
        - width (int): the width of the rectangle
        - height (int): the height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
