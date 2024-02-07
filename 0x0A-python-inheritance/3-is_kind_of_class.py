#!/usr/bin/python3
"""Defines a function to check if an object is an instance of, or inherited from, a specified class."""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if the object is an instance of `a_class` or inherited from it, otherwise False.
    """
    return isinstance(obj, a_class)
