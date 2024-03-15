#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """
    Square each element of a matrix using map function.

    Args:
        matrix (list of lists): The matrix to be squared.

    Returns:
        list of lists: The matrix with each element squared.
    """
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
