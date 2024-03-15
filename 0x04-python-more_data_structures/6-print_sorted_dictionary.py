#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints the key-value pairs of a dictionary sorted by keys.

    Args:
        a_dictionary (dict): The input dictionary to be printed.

    Returns:
        None
    """
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for i in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
