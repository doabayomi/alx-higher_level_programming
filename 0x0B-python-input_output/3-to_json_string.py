#!/usr/bin/python3
"""Returns the JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj (object): The object in question

    Returns:
        str: The JSON representation of the object
    """
    json_repr = json.dumps(my_obj)
    return json_repr
