#!/usr/bin/python3
"""Reads the contents of a file and print to stdout."""


def read_file(filename=""):
    """Read the contents of a file and print to stdout.

    Args:
        filename (str): The name fo the file
    """
    with open(filename, encoding="utf-8") as f:
        file_data = f.read()
    print(file_data, end="")
