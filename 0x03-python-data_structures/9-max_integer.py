#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        num = my_list[0]
        for i in range(1, len(my_list)):
            if num < my_list[i]:
                num = my_list[i]
        return num
    else:
        return None
