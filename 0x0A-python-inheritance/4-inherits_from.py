#!/usr/bin/python3

"""Module for the function inherit_from"""


def inherits_from(obj, a_class):
    """Function that checks if an object is an instance of a class
    that inherited from specific class

    Args:
    obj: object to chech
    a_class: class specified

    Returns: True or False

    """
    return isinstance(obj, a_class) and type(obj) is not a_class
