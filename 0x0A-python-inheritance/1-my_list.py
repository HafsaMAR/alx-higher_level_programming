#!/usr/bin/python3

"""The module about public instance methode print_sorted"""


class MyList(list):
    """ class my list """

    def print_sorted(self):
        """methode that print list in sorted order"""
        self.sort()
        print(self)
