#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    calcu = len(sys.argv) - 1
    if calcu == 0:
        print("0 arguments.")
    elif calcu == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(calcu))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
