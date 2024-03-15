#!/usr/bin/python3
def uniq_add(my_list=None):
    if my_list is None:
        my_list = []

    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return num
