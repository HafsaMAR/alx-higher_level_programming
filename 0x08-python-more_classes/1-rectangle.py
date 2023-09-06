#!/usr/bin/python3
"""This module is for the class Rectangle"""


class Rectangle:
    """Rectangle class that initialize a rectangle"""

    def __init__(self, width=0, height=0):
        """Methode that define the instances
        Args:
        width (int): the witdh of the rectangle
        height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Methode to retrieve the width of the rectangle
        Returns:
            the width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that returns the value of the height

        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
