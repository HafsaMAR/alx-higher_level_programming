#!/usr/bin/python3

"""Module for class_to_json function"""


def class_to_json(obj):
    """
    Function that returns a dictionary description for
    JSON serialization of the object

    Args:
        obj: Class instance
    Returns:
        dictionary description
    """
    return obj.__dict__
