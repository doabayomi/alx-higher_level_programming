#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_len = len(my_list)
    for i in range((my_list_len - 1), -1, -1):
        print("{0:d}".format(my_list[i]))
