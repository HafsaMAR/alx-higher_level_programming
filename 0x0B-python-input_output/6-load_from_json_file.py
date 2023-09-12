#!/usr/bin/python3

"""Module for load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Function that create an object from a JSON file

    Args:
        filename: file

    Returns:
        object
    """
    with open(filename, "r", encoding="UTF8") as f:
        return json.load(f)
