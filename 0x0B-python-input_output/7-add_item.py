#!/usr/bin/python3
"""Module for a script that adds the arguments
to a pyhton list and save them in a file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(arg):
    """adds all arguments passed to list and write it to json file

    Args:
        arg: argment passed
    """
    filename = "add_item.json"
    try:
        arg_list = load_from_json_file(filename)

    except FileNotFoundError:
        arg_list = []

    for i in range(1, len(arg)):
        arg_list.append(arg[i])
        save_to_json_file(arg_list, filename)


if __name__ == "__main__":
    add_item(sys.argv)
