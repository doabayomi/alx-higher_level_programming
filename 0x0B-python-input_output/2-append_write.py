#!/usr/bin/python3
"""Appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file.

    Args:
        filename (str): The name of the file
        text (str): The text to add.

    Returns:
        int: The number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        character_count = f.write(text)
    return character_count
