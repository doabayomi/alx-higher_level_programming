#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for i in range(len(str)):
        char = str[i]
        if (i == n):
            continue
        str_cpy = str_cpy + char
    return str_cpy
