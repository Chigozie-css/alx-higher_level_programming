#!/usr/bin/python3

"""
This module contains a function that divides all elements of a matrix.

"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide each element of the matrix.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                    if each row of the matrix doesn't have the same size,
                    or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    """
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]

# Test cases
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    result = matrix_divided(matrix, 3)
    print(result)
    print(matrix)
