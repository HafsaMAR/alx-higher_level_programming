#!/usr/bin/python3

"""Module for wirte_file function"""


def write_file(filename="", text=""):
    """
    Function that write into a file
    and returns the number of characters written

    Args:
        filename: file object to write into
        text: string to be writen

    Return: number if characters written
    """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
