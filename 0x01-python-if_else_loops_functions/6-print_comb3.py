#!/usr/bin/python3
for ten in range(8):
    for unit in range(ten + 1, 10):
        print("{}{}".format(ten, unit), end=', ')
print("{}".format(89))
