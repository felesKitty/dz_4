from itertools import count
from math import factorial


def fact():
    for i in count(1):
        yield factorial(i)


x = 0
for v in fact():
    if x == 25:
        break
    else:
        x += 1
        print(f'{x}! = {v}')
