#!/usr/bin/python3

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
