#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Finds if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (object): The object in question
        a_class (class): The class to confirm membership of

    Returns:
        (bool): True  if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class, False
        otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
