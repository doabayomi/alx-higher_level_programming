#!/usr/bin/python3
def multiple_returns(sentence):
    try:
        first_char = sentence[0]
    except (IndexError, TypeError):
        first_char = None

    try:
        str_len = len(sentence)
    except (IndexError, TypeError):
        str_len = 0

    ret_tuple = (str_len, first_char)
    return ret_tuple
