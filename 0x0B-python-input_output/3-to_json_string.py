#!/usr/bin/python3

"""Module for the to_json_string function"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an objet
    Args:
        my_obj: object to serialize

    Returns:
        string representation of the object
    """
    import json
    return json.dumps(my_obj)
