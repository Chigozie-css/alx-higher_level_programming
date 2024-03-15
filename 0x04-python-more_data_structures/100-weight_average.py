#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of tuples.

    Args:
        my_list (list): List of tuples where each tuple contains two elements: (value, weight).

    Returns:
        float: The weighted average.
    """
    if not my_list:
        return 0

    num = 0
    den = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return num / den
