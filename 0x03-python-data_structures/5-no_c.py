#!/usr/bin/python3
def no_c(my_string):
    filtered = ""
    for char in my_string:
        if char not in "cC":
            filtered += char
    return filtered
