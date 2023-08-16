#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = list(map(list, map(lambda row: map(lambda element: element ** 2, row), matrix)))
    return square_matrix
