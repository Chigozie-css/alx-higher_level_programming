#!/usr/bin/python3
import sys
import json

def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file using a JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to save the JSON representation to.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """
    Create an object from a Json file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)

def add_items_to_list(filename, *args):
    """
    Add items to a Python list and save them to a JSON file.

    Args:
        filename (str): The name of the JSON file to load/save.
        args (list): The items to add to the list.
    """
    try:
        existing_list = load_from_json_file(filename)
    except FileNotFoundError:
        existing_list = []

    updated_list = existing_list + list(args)
    save_to_json_file(updated_list, filename)

if __name__ == "__main__":
    filename = "add_item.json"
    add_items_to_list(filename, *sys.argv[1:])
