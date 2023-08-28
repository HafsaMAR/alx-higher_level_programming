#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for counter in range(x):
        try:
            print("{:d}".format(my_list[counter]), end='')
            counter += 1
        except (ValueError, TypeError):
            counter += 1
        except IndexError:
            raise
    print()
    return counter
