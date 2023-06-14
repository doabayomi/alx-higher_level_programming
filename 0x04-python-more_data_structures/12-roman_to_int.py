#!/usr/bin/python3
def roman_to_int(roman_string):
    reference = {'I': 1, 'X': 10, 'V': 5, 'L': 50, 'C': 100, 'D': 500}
    reference.update({'M': 1000})

    numerals = reference.keys()
    integer = 0
    try:
        for ind, numeral in enumerate(roman_string):
            if numeral in numerals:
                try:
                    next_numeral = roman_string[ind + 1]
                except IndexError:
                    next_numeral = None

                value = reference.get(numeral)
                next_value = reference.get(next_numeral)
                if next_value == None:
                    integer = integer + value
                elif next_value > value:
                    integer = integer - value
                elif next_value <= value:
                    integer = integer + value
            else:
                return 0
    except TypeError:
        return 0
    return integer
