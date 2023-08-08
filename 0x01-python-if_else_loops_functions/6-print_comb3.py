#!/usr/bin/python3
for ten in range(9):
    for unit in range(ten + 1, 9):
        print("{}{}".format(ten, unit), end=', ')
print("{}".format(89))
