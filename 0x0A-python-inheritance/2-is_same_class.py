#!/usr/bin/python3
"""Module to find if an object is an exact instance of a specified class
"""


def is_same_class(obj, a_class):
    """Finds if the object is exactly an instance of the specified class

    Args:
        obj (object): The object in question
        a_class (class): The class to confirm membership of

    Returns:
        (bool): True if object is exactly an instance of specified
    """
    if type(obj) == a_class:
        return True
    else:
        return False
