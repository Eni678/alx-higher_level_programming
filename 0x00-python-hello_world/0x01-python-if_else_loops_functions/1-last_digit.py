#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = number

if number < 0:
    number = -(number)
lastdigit = number % 10
if last_number < 0:
    number = last_number
    lastdigit = -(lastdigit)

if lastdigit > 5:
    string = "and is greater than 5"
elif lastdigit == 0:
    string = 'and is 0'
elif lastdigit < 6:
    string = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, lastdigit), string)
