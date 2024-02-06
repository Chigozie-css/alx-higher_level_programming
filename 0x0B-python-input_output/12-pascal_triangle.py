#!/usr/bin/python3
"""Defines a function to generate Pascal's Triangle."""

def pascal_triangle(n):
    """Generate Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return[]

    triangle = [[1]]
    while len(triangle) < n:
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
