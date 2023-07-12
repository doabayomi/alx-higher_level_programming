#!/usr/bin/python3
"""Writes the contents of a file and returns number of characters printed."""


def write_file(filename="", text=""):
    """Write the contents of a file and returns no of characters printed.

    Args:
        filename (str): The name of the file
        text (str): The text to add.

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        characters_count = f.write(text)
    return characters_count
