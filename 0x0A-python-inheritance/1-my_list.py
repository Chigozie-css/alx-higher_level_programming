#!/usr/bin/python3

class MyList(list):
    """Inherits from list with additional method."""
    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
