#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "estEulerConst.py", "7/06/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from math import factorial
from time import clock

# SUM <1/(n!)>
def e_nth(n):
    return 1/factorial(n)


def mc_e(degree):
    current = 0

    for n in range(degree):
        current += e_nth(n)

    return current

start = clock()
pi = mc_e(15000)
time = clock() - start
print(pi)
print("Done in {} seconds".format(time))


# 2.718281828459045 23536028747135266249775724709369995
#                  ^15000 iterations of series in 34.4 seconds




