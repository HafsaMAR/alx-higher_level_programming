#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f'%s is positive' % number)
elif number == 0:
    print('{} is zero'.format(number))
else:
    print('{} is negative'.format(number))
