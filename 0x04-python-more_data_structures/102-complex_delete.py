#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Delete keys from a dictionary based on their corresponding values.

    Args:
        a_dictionary (dict): The dictionary to delete keys from.
        value: The value to search for and delete its corresponding keys.

    Returns:
        dict: The dictionary after deleting keys with the specified value.
    """
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return a_dictionary
