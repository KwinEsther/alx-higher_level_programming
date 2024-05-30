#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    L = number % 10

else:
    number = number * -1
    L = (number % 10) * -1
    number = number * -1

if L > 5:
    print(f"Last digit of {number} is {L} and" + " is greater than 5")
elif L == 0:
    print(f"Last digit of {number} is {L} and is 0")
else:
    print(f"Last digit of {number} is {L} and is" + " less than 6 and not 0")
