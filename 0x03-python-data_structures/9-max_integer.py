#!/usr/bin/python3
def max_integer(my_list=[]):
    try:
        max_value = my_list[1]
    except IndexError:
        return None

    for num in my_list:
        if max_value > num:
            continue
        else:
            max_value = num
    return max_value
