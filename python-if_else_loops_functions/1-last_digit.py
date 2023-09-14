#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit = num_str[-1]
x = int(last_digit)

if x == 0:
    print(f"Last digit of {number} is {x} and is 0")
elif x > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")
else:
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
