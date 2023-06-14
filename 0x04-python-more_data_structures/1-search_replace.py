#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for i, number in enumerate(my_list):
        if number == search:
            new_list[i] = replace
        else:
            continue
    return new_list
