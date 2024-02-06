#!/usr/bin/python3

def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file using a JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to save the JSON representation to.
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
