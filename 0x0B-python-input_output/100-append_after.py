#!/usr/bin/python3

"""Module for the append_after funtion"""


def append_after(filename="", search_string="", new_string=""):
    """
    insert new string after each line containing a searched string

    Args:
        filename: name of the file
        search_string (str): string to look for
        new_string (str): string to add after searched string

    """
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        new = []
        for line in lines:
            new.append(line)
            if search_string in line:
                new.append(new_string)
        f.seek(0)
        f.writelines(new)
