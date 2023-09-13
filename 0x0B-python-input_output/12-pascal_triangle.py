#!/usr/bin/python3

"""Module for pascal_triangle function"""


def pascal_triangle(n):
    """
    return list of lists of integers representing
    the triangle of pascal
    
    Args:
        n (int): the number
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for j in range(1, n):
        row = [1]
        for i in range(1, j):
            row.append(triangle[j - 1][i - 1] + triangle[j - 1][i])
        row.append(1)
        triangle.append(row)
    return triangle