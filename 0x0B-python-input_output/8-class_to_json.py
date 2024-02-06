#!/usr/bin/python3
"""Defines a function to convert a Python class instance to JSON."""


def class_to_json(obj):
    """Convert a Python class instance to a dictionary representation."""
    return obj.__dict__
