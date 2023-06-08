#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_count = len(argv)
    if (arg_count < 2):
        print("0")
    else:
        total = 0
        for i in range(1, arg_count):
            n = int(argv[i])
            total = total + n
        print(total)
