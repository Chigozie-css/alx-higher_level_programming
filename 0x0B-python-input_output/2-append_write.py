#!/usr/bin/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-append_write.txt")
