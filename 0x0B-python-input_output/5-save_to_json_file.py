#!/usr/bin/python3

"""Module for save_to_json function"""


def save_to_json_file(my_obj, filename):
    """
    Function that write JSON representation into a file

    my_obj: python data structure
    filename: file

    Returns:
        None
    """
    import json
    with open(filename, "w", encoding="UTF8") as f:
        json.dumps(my_obj, f)
