#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
sign = "" if number > 0 else "-"
limit = "greater than 5" if last > 5 else "0" if last == 0 else "less than 6 and not 0"
print(f"Last digit of {number} is {sign}{last} and is not {limit}")
