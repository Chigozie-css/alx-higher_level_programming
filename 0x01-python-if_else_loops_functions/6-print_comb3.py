#!/usr/bin/python3
a = 0
for a in range(0, 8):
    for b in range(a + 1, 10):
        print("{:d}{:d}".format(a, b), end=", ")
a += 1
b -= 1
print("{:d}{:d}".format(a, b + 1), end="\n")
