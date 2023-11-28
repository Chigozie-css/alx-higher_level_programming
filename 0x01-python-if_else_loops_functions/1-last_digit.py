#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
sign = "-" if number < 0 else "-"
out_str = f"Last digit of {number} is {sign}{last}"

if last > 5:
    out_str += " and is greater than 5"
elif last == 0:
    out_str += " and is 0"
else:
    out_str += " and is less than 6 and not 0"
print(out_str)
