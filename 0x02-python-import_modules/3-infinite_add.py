#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print(0)
    else:
        result = 0
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
        print("{}".format(result))
