#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_list = set()
    list(map(lambda element: new_list.add(
        element) if element in set_2 else None, set_1))
    return new_list
