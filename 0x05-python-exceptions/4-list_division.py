#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element-wise.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length `list_length` containing all the divisions.
        If any element in `my_list_2` is zero or the lists are of different lengths, 
        it returns 0 for the corresponding element in the result list.
        If any element in either list is not a number (e.g., string), it returns 0 for that element.
    """
    result_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Element at index {} is not a number. Setting division result to 0.".format(i))
            div = 0
        except ZeroDivisionError:
            print("Division by 0 at index {}. Setting division result to 0.".format(i))
            div = 0
        except IndexError:
            print("Index out of range for index {}. Setting division result to 0.".format(i))
            div = 0
        finally:
            result_list.append(div)
    return result_list
