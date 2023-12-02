#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list.copy()
    reversed_list.reverse()
    for element in reversed_list:
        print("{:d}".format(element))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
