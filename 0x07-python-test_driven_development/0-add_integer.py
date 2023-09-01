#!/usr/bin/python3
"""
This module contains a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    This function adds 2 integers.
    Args:
        a : first int.
        b : second int.
    Return:
        int: sum of a and b.
    Raises:
        TypeError: if either a or b is not int or float.
    """
    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
