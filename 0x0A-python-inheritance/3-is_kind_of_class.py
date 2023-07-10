#!/usr/bin/python3
"""Module to find if an object is an inherited instance or derived instance
of a specified class
"""


def is_kind_of_class(obj, a_class):
    """Finds if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj (object): The object in question
        a_class (class): The class to confirm membership of

    Returns:
        (bool): True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class, False
        otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
