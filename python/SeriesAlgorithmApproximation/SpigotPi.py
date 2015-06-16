#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "SpigotPi.py", "8/06/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from math import factorial
from time import clock

def get_pi_d(d):
    """
    (16^d)pi = 4*((16^d) * S1) - 2*((16^d) * S4) - ((16^d) * S5) - ((16^d) * S6)
    where Sj = SUM 1 / (16^k * (8k + j))
    """
    s1 = series(d, 1)
    s2 = series(d, 4)
    s3 = series(d, 5)
    s4 = series(d, 6)

    pi_digit = 4*s1 - 2*s2 - s3 - s4
    # pi_digit -= int(pi_digit) + 1

    return pi_digit

def series(d, j):
    """
    SUM K -> d of (16^(d-k) mod(8k + j)) / (8k + j) + SUM k=d+1 -> infinity of 16^(d-k) / (8k + j)

    """
    # Sum series to n
    sum = 0
    for k in range(d):  # d - 1?
        denom = 8*k + j
        pow = d - k
        term = modpow16(pow, denom)
        sum += term/denom
        sum -= int(sum)

    return 0

def modpow16(p, m):
    if m == 1:
        return 0

def spig_nth(n):
    # SUM <1/16^n(4/(8n + 1) - (2/8n + 4) - (1/8n + 5) - (1/8n + 6)))>
    return (1 / (16**n)) * ((4 / (8*n + 1)) - (2 / (8*n + 4)) - (1 / (8*n + 5)) - (1 / (8*n + 6)))

def spig(degree):
    current = 0

    for n in range(degree):
        current += spig_nth(n)

    return current

# start = clock()
# pi = spig(200)
# time = clock() - start
# print(pi)
# print("Done in {} seconds".format(time))
# print()

print(get_pi_d(5))





