#!/usr/bin/python3

def no_c(my_string):
    char_list = list(my_string)
    for c in my_string:
        if c in "cC":
            char_list.remove(c)
    return ''.join(char_list)
