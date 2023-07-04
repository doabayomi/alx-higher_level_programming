#!/usr/bin/python3
"""Breaks text using breakpoints
"""


def text_indentation(text):
    """Adds new lines after certain characters

    Args:
        text (str): The body text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "" or text[0] == '\0':
        print("", end="")
    characters = ['.', '?', ':']
    i = 0
    while i < len(text):
        if i == 0 and text[i] == " ":
            while i < len(text) and text[i] == " ":
                i += 1
        if i > 0 and text[i - 1] in characters:
            print("\n")
            while i < len(text) and text[i] == " ":
                i += 1
        print(text[i], end="")
        i += 1

    if text[i - 1] in characters:
        print("\n")
