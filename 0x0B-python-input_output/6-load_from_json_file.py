#!/usr/bin/python3
"""Creates an object from a json file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The name of the file

    Returns:
        obj: The created object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data
