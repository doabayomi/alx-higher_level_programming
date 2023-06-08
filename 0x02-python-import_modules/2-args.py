#!/usr/bin/python3
from sys import argv as argv
if __name__ == "__main__":
    arg_count = len(argv)
    if (arg_count < 2):
        print("0 arguments.")
    elif (arg_count == 2):
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))

    for i in range(1, arg_count):
        print("{0}: {1}".format(i, argv[i]))
