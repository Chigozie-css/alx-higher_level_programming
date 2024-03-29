#!/usr/bin/python3
def weight_average(my_list=[]):
    return sum(x * y for x, y in my_list) / sum(y for _, y in my_list) if my_list else 0
