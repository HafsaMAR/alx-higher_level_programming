#!/usr/bin/python3

"""Module for form_json_string function"""


def from_json_string(my_str):
    """
    Function that convert a string to a python data structure

    Args:
        my_str: string json representation

    Returns:
        python data structure
    """
    import json
    from io import StringIO
    io = StringIO(my_str)
    return json.load(io)
