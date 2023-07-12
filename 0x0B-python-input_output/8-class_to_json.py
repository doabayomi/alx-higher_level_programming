#!/usr/bin/python3
"""Converts a class to JSON dictionary."""


def class_to_json(obj):
    """Convert an object to a JSON serializable dictionary.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    attributes = vars(obj)
    json_dict = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
