#!/usr/bin/python3
"""Defines a Json to object function."""

def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to an object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    import json
    return json.loads(my_str)
