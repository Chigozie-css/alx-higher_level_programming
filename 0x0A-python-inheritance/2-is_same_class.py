#!/usr/bin/pythin3

"""Defines a class-checking function."""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if the object is exactly an instance of `a_class`, otherwise False.
    """
    return type(obj) is a_class
