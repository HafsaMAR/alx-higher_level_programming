#!/usr/bin/python3

"""Module for the function say_my_name.
"""

def say_my_name(first_name, last_name=''):
    """Function that prints my name is <first_name> <last_name>.
    
    Args:
        first_name(str): the first name.
        last_name(str): the last name.
        
    Returns:
        None.
    
    Raises:
        TypeError: if firstname or last name are not str.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
