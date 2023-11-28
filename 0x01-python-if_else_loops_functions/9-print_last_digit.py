#!/usr/bin/python3
def print_last_digit(number):
    '''prints the last digit of a number'''
    last_number = abs(number) % 10
    print("{:d}".format(last_number), end="")
    return last_number
