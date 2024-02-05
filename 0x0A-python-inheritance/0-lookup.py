#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an objects.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the name of attributes and methods.

    """

    return dir(obj)

if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
