#!/usr/bin/python3
"""Adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int): The first number
        b (int): The second number
    """
    if (not isinstance(a, int)) or (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) or (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
