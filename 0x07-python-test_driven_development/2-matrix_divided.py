#!/usr/bin/python3
"""

This module provides a function for dividing elements of a matrix.

"""


def matrix_divided(matrix, divisor):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists representing the matrix.
        divisor: The number to divide each matrix element by.

    Raises:
        TypeError: If matrix contains non-numeric values or rows of different sizes.
        TypeError: If divisor is not a number (int or float).
        ZeroDivisionError: If divisor is zero.

    Returns:
        A new matrix representing the result of the divisions.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("Matrix must be a list of lists containing integers or floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(divisor, int) and not isinstance(divisor, float):
        raise TypeError("Divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("Division by zero")

    return ([list(map(lambda x: round(x / divisor, 2), row)) for row in matrix])
