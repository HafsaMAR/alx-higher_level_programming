#!/usr/bin/python3

"""Module for the function is_same_class"""


def is_same_class(obj, a_class):
    """Function that checks if an object in exactly an instance of a specific class

    Args:
    obj: object to chech
    a_class: class specified
    
    Returns: True or False

    """
    return type(obj) is a_class
