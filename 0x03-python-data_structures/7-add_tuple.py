#!/usr/bin/python3
def sum_member(ind, tuple_a={}, tuple_b=()):
    try:
        first_number = int(tuple_a[ind])
    except IndexError:
        first_number = 0

    try:
        second_number = int(tuple_b[ind])
    except IndexError:
        second_number = 0

    return (first_number + second_number)


def add_tuple(tuple_a=(), tuple_b=()):
    first_member = sum_member(0, tuple_a, tuple_b)
    second_member = sum_member(1, tuple_a, tuple_b)
    sum_tuple = (first_member, second_member)
    return sum_tuple
