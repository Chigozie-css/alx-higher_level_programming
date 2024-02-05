#!/usr/bin/python3
\
"""Defines an inherited list class MyList."""

class MyList(list):
    """Inherits from list with additional method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
