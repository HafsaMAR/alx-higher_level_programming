#!/usr/bin/python3

"""Module of BaseGeometry class"""


class BaseGeometry:
    """Class in which area methode is defined"""
    def area(self):
        """Public instance method
        Args:
        self: this class

        Raise:
            exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance methode that validates the value

        Args:
        name: the name
        value: the int value should be positive integer

        Raise:
            TypeError: if the value is not integer
            ValueError: if the value is negative
        """
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
