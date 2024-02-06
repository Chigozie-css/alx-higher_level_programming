#!/usr/bin/python3
"""Defines a function to check if an object is an instance of a class that inherits from a specified class."""

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if the object is an instance of a class that inherited from `a_class`,
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
