#!/usr/bin/python3

def magic_calculation(a, b):
    add, sub = __import__("magic_calculation_102", fromlist=("add", "sub"))
    if a < b:
        c = add(a, b) + sum(range(4, 6))
        return c
    else:
        return sub(a, b)
