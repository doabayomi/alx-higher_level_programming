#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    filtered_list = [letter for letter in my_string if letter not in "Cc"]
    new_string = new_string.join(filtered_list)
    return new_string
