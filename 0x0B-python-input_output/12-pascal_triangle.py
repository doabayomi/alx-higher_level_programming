#!/usr/bin/python3
"""Returns a list of lists integer representing a pascal trangle."""


def factorial(a):
    """Find the factorial of a number.

    Args:
        a (int): The number whose factorial is to be found

    Returns:
        (int): The factorial of the number
    """
    total = 1
    for i in range(1, (a + 1)):
        total = total * i
    return total


def combination(n, r):
    """Find the nCr of a number.

    Args:
        n (int): Number
        r (int): Number to find combination to

    Returns:
        int: nCr of the number
    """
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    nCr = n_factorial / (factorial(n - r) * r_factorial)
    return nCr


def pascal_triangle(n):
    """Create a pascal triangle as a list of lists.

    Args:
        n (int): Number of rows

    Returns:
        list: The list of lists representation
    """
    triangle = []
    for i in range(0, (n + 1)):
        row = []
        for j in range(0, (i + 1)):
            row.append(combination(i, j))
        triangle.append(row)
    return triangle
