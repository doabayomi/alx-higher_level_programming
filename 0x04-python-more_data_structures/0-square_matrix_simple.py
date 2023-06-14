#!/usr/bin/python3
def square(x):
    return (x * x)


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        tmp_list = []
        for element in row:
            squared_element = square(element)
            tmp_list.append(squared_element)
        new_matrix.append(tmp_list)
    return new_matrix
