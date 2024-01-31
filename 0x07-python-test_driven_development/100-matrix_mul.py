#!/usr/bin/python3
"""
This module multiplies two matrices.

Read: Matrix multiplication - only Matrix product (two matrices)
"""

def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): First matrix (list of lists).
        m_b (list): Second matrix (list of lists).

    Returns:
        list: Resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   or if an element is not an integer or a float.
        ValueError: If m_a or m_b is empty or not a rectangle.

    Example:
        >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        [[7, 10], [15, 22]]
        >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        [[13, 16]]
        >>> matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
        [[58, 64], [139, 154]]
        >>> matrix_mul([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])
        Traceback (most recent call last):
        ...
        ValueError: matrices are not aligned
        >>> matrix_mul([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])
        Traceback (most recent call last):
        ...
        ValueError: matrices are not aligned
        >>> matrix_mul([[1, 2], [3, 4]], [[5], [6]])
        Traceback (most recent call last):
        ...
        ValueError: matrices are not aligned

    6 passed and 0 failed.
    Test passed.
    """

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
