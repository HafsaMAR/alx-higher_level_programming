#!/usr/bin/python3

"""Module for text_indentation function."""

def text_indentation(text):
    """This funtion prints a text with 2 new lines after each of these 
    characters: ., ? and :.

    Args:
    text(str): text to be splited.

    Return:
        None.
    
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for delim in "?.:":
        text = (delim + '\n\n').join([line.strip(" ") for line in text.split(delim)])