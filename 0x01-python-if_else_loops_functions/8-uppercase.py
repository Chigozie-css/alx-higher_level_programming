#!/usr/bin/python3
def uppercase(s):
    for ch in s:
        if 97 <= ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print("{:s}".format(ch), end="")
    print("\n", end="")
