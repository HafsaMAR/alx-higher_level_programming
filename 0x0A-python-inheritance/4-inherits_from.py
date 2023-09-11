#!/usr/bin/python3

"""Module for the function is_kind_of_class"""


def inherits_from(obj, a_class):
    """Function that checks if an object is an instance of a specific class

    Args:
    obj: object to chech
    a_class: class specified

    Returns: True or False

    """
    return isinstance(obj, a_class) and type(obj) != a_class