#!/usr/bin/python3
"""Dividing elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divides a matrix by an integer

    Args:
        matrix (list): A matrix of floats/integers
        div (float): The divisor

    Returns:
        The divided matrix
    """
    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    not_int_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_msg = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list):
        raise TypeError(not_int_msg)
    if not matrix:
        raise TypeError(not_int_msg)
    for row in matrix:
        divided_row = []
        for i in row:
            if (not isinstance(i, int)) and (not isinstance(i, float)):
                raise TypeError(not_int_msg)
            divided_row.append(round(i / div, 2))
        for others in matrix:
            if (len(row) != len(others)):
                raise TypeError(size_msg)
        divided_matrix.append(divided_row)
    return divided_matrix
