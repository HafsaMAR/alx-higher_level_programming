#!/usr/bin/python3

def uppercase(str):
    result = ""
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            diff = ord('A') - ord('a')
            result += chr(ord(letter) + diff)
        else:
            result += letter
    print("{}".format(result))
