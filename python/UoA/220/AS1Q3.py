#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "AS1Q3.py", "16/03/16", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


def T(n):
    if n <= 1:
        return 0
    # print(n)
    return 3*T(n/3) + 6

x = 3**3

# print(T(x))
# print(3*x - 3)

for i in range(10):
    actual = T(3**i)
    guess = 3*(3**i) - 3

    print("n = {}, guessed {}".format(actual, guess))
    if guess != actual:
        print("FAIL")
        exit()

# print(6 * (3*x-1)/2.0)


