#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "AS1q1.py", "16/03/2016", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


def sign_magnitude(number, bits):
    bin_num = ['0'] * bits

    max_mag = 2**(bits-1) - 1

    bin_num[0] = str(int(number < 0))
    number = abs(number)

    if number > max_mag:
        return None

    i = 1
    while i < bits:
        # print(number % 2)
        bin_num[bits-i] = str(number % 2)
        number //= 2
        i += 1

    return "".join(bin_num)

print(sign_magnitude(27, 6))
print(sign_magnitude(-27, 6))

print(sign_magnitude(27, 5))

print(sign_magnitude(0, 16))

print(sign_magnitude(-16, 5))

print(sign_magnitude(-10000, 16))