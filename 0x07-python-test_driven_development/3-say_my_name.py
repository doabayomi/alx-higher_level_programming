#!/usr/bin/python3
"""Say my name functionally
"""


def say_my_name(first_name, last_name=""):
    """Says someone's name

    Args:
        first_name (str): The first name of the person
        last_name (str): The last name of the person
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
