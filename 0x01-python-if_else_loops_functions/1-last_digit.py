#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = number
if Last_digit % 10 == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif Last_digit < 0:
    print("Last digit of {:d} is -{:d} and is less than 6 and not 0".format
        (number, abs(Last_digit) % 10))
elif abs(Last_digit % 10) < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format
        (number, Last_digit % 10))
else:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,
        Last_digit % 10))

