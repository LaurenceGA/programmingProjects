#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "SpigotPi.py", "8/06/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from math import factorial
from time import clock

# SUM <1/16^n(4/(8n + 1) - (2/8n + 4) - (1/8n + 5) - (1/8n + 6)))>
def spig_nth(n):
    return (1 / (16**n)) * ((4 / (8*n + 1)) - (2 / (8*n + 4)) - (1 / (8*n + 5)) - (1 / (8*n + 6)))


def spig(degree):
    current = 0

    for n in range(degree):
        current += spig_nth(n)

    return current

start = clock()
pi = spig(20)
time = clock() - start
print(pi)
print("Done in {} seconds".format(time))







