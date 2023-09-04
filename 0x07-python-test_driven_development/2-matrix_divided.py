#!/usr/bin/python3

"""Module for matrix_divided function"""


def matrix_divided(matrix, div):
    """
    Function that divides the elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): the divisor.

    Returns:
        list: matrix containing the result of the division

    Raises:
        TypeError: If matrix is not a list of lists of int or float
        TypeError: IF the rows of the matrix are of different sizes
        TypeError: If division is not an integer or float.
        ZeroDivisionError: IF div is 0
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not (isinstance(item, int) or (isinstance(item, float))):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    return [[round(item / div, 2) for item in row] for row in matrix]
