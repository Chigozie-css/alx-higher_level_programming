#!/usr/bin/python3
"""Defines a function for object attribute lookup."""

def lookup(obj):
    """Return a list of an object available attributes."""
    return dir(obj)
