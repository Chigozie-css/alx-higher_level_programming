#!/usr/bin/python3
"""Defines a Json file reading function"""

def load_from_json_file(filename):
    """
    Create an object from a Json file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        import json
        return json.load(f)

