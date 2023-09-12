#!/usr/bin/python3

"""Module for append_write"""


def append_write(filename="", text=""):
    """Function that append text to a file and return
    the number of characters printed
    Args:
        filename: object file to write into
        text : string to append

    Returns:
        number of characters printed
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
