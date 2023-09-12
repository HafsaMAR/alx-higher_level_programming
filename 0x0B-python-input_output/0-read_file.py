#!/usr/bin/python3

"""Module for the read_file method"""


def read_file(filename=""):
    """Function that reads the text file and prints it to stdout
    
    Args:
        filename: file object to read
    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
