#!/usr/bin/python3

letter = 'z'
while letter >= "a":
    uppercase_letter = letter.upper() if ord(letter) % 2 != 0 else letter
    print("{}".format(uppercase_letter), end="")
    letter = chr(ord(letter) - 1)

