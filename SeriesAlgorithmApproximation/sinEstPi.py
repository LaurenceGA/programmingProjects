#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "sinEstPi.py", "4/06/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from math import factorial
from time import clock

# McLaurin series of arcsin(x) is SUM <(2n)! * x^(2n + 1) / (2^n * n!)^2 * (2n + 1)>
# arcsin(1) = pi/2
"""
def factorial(n):
    if n < 2:
        return 1

    final = 1

    for i in range(2, n+1):
        final *= i

    return final
"""
def arcsin_nth(n, value):
    return (factorial(2*n) * value**(2*n + 1)) / ((2**n * factorial(n))**2 * (2*n + 1))


def mc_arcsin(degree, value):
    current = 0

    for n in range(degree):
        current += arcsin_nth(n, value)

    return current

start = clock()
pi = 2*mc_arcsin(3000, 1)
time = clock() - start
print(pi)
print("Done in {} seconds".format(time))



