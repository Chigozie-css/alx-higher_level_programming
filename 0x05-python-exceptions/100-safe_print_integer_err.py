#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Safely prints an integer.

    Tries to print the value as an integer followed by a newline.
    If successful, returns True; if not (due to TypeError or ValueError),
    prints an error message to stderr starting with "Exception:" and returns False.

    Args:
        value: The value to print.

    Returns:
        bool: True if printing succeeds, False otherwise.
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except (TypeError, ValueError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
