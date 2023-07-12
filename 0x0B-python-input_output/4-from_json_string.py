#!/usr/bin/python3
"""Returns the object representation of JSON string."""
import json


def from_json_string(my_str):
    """Return the object represnentation of a JSON string.

    Args:
        my_str (str): The JSON representation of the object

    Returns:
        obj: The python data structure equivalent
    """
    obj_repr = json.loads(my_str)
    return obj_repr
