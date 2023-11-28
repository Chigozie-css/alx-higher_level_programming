#!/usr/bin/python3
def magic_calculator(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
