#!/usr/bin/python3
"""Module to print members and methods of an object
"""


def lookup(obj):
    """Prints the members and methods of an object

    Args:
        obj (class): The object to print for

    Returns:
        (list): The list of all the members and methods in the object
    """
    return dir(obj)
