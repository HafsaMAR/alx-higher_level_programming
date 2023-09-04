#!/usr/bin/python3

"""Module for print_square function"""


def print_square(size):
    """This function prints a square with the character #.
    
    Args:
        size(int): the width of the square.
        
    Returns:
        None.
        
    Raises:
        TypeError: if size is not integer.
        ValueError: if size is not positive integer.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()    