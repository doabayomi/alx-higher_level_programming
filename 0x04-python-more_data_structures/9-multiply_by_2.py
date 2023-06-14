#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_keys = a_dictionary.keys()
    new_dict = {}
    for key in dict_keys:
        val = a_dictionary.get(key)
        val = val * 2
        new_dict[key] = val
    return new_dict
