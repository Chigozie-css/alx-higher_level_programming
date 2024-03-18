#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Safely prints an integer.

    Attempts to print the provided integer value using "{:d}".format().
    If successful, returns True. If an error occurs (TypeError or ValueError),
    prints an error message to stderr and returns False.

    Args:
        value (int): The integer value to print.

    Returns:
        bool: True if printing succeeds, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return False
