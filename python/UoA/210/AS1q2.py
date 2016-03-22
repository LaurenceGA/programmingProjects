#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "AS1q2.py", "16/03/2016", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


def add_overflow(a, b, bits):
    bits_num = int('1' * bits, 2)

    bin_a = format(a & bits_num, "0" + str(bits) + "b")
    bin_b = format(b & bits_num, "0" + str(bits) + "b")
    sm = a + b
    bin_sum = format(sm & bits_num, "0" + str(bits) + "b")

    overflow = ""
    if sm > 2**(bits-1) - 1 or sm < -2**(bits-1):
        overflow = " overflow"

    print("{} + {} = {}{}".format(bin_a, bin_b, bin_sum, overflow))

add_overflow(-1, -1, 2)
