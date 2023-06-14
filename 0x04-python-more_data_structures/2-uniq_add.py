#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    for i, val in enumerate(my_list):
        if val not in my_list[:i]:
            uniq_sum = uniq_sum + val
        else:
            continue
    return uniq_sum
