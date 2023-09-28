#!/usr/bin/python3
"""Finding the peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find the peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers

    Returns:
        int: The peak/highest value in the list
    """
    if not list_of_integers:
        return None
    
    peak = list_of_integers[0]
    for n in list_of_integers:
        if n > peak:
            peak = n
    
    return peak
