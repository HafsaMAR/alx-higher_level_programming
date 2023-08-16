#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_list = set()
    return sum(map(lambda x: x if x not in unique_list and not unique_list.add(
        x) else 0, my_list))
