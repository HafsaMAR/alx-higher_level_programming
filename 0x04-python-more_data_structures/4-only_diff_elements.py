#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    result = set()
    list(map(lambda element: result.add(
        element) if element not in set_2 else None, set_1))
    list(map(lambda element: result.add(
        element) if element not in set_1 and element not in result else None,
        set_2))
    return result
