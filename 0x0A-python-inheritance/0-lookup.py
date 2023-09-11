#!/usr/bin/python3

"""This module is about the function lookup"""


def lookup(obj):
    """This function returns a list of available attributes
    and methods of an object

    Args:
    obj: object in question

    Returns:
    list of available attributes and methodes

    """
    return dir(obj)
