#!/usr/bin/python3

import os

def easy_print(message):
    os.write(1, message.encode())

easy_print("#pythoniscool\n")