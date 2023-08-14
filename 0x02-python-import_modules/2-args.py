#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    num_arguments = len(sys.argv)
    if num_arguments == 1:
        print("0 arguments.")
    elif num_arguments == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
            print("{} arguments:".format(num_arguments - 1))
            for i in range(1, num_arguments):
                print("{}: {}".format(i, sys.argv[i]))
