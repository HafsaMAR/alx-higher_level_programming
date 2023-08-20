#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    number = 0
    less_than_num = 0
    
    for char in roman_string:
        numeric_value = roman_dict.get(char, None)
        
        if numeric_value is not None:
            if less_than_num != 0:
                less_than_num = numeric_value
            if less_than_num < numeric_value and less_than_num in [100, 10, 1]:
                number -= less_than_num
            else:
                number += numeric_value
            less_than_num = numeric_value
    return number

