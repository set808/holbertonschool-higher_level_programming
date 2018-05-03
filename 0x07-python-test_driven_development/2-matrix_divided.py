#!/usr/bin/python3


def matrix_divided(matrix, div):
    if isinstance(matrix, list) is False or \
       all(isinstance(row, list) for row in matrix) is False:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if len(matrix) == 0 or all(len(row) == 0 for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if all(len(row) == len(matrix[0]) for row in matrix) is False:
        raise TypeError('Each row of the matrix must have the same size')
    if isinstance(div, (int, float)) is False:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(x / div, 2) for x in row] for row in matrix]
