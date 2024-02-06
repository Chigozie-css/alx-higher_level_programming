#!/usr/bin/python3
"""Defines a function to append text after each occurrence of a specified string in a file."""

def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
    filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    appended_text = ""
    with open(filename) as file:
        for line in file:
            appended_text += line
            if search_string in line:
                appended_text += new_string
    with open(filename, "w") as file:
        file.write(appended_text)
