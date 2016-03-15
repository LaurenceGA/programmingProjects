#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "AS1.py", "13/03/2016", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import math

n = 7

i = 1
outer_counter = 0
f1_count = 0
f2_count = 0
true_for_count = 0
false_for_count = 0

operations = 0

while i < 2**n:
    outer_counter += 1

    if i <=4 or i >= 2**(n-2):
        f1_count += 1

        j = n
        while j >= 0:
            j -= 2
            operations += 1
            true_for_count += 1
    else:
        f2_count += 1
        j = n
        while j > 1:
            j /= 2
            operations += 1
            false_for_count += 1

    i *= 2

# print("n:", n)
# print("Expected operations: ", (n-5) * math.ceil(math.log(n, 2)) + 6*(math.floor(n / 2) + 1))
# print("outer loop:", outer_counter)
# print("if true:", f1_count)
# print("if false:", f2_count)
# print("if true for:", true_for_count)
# print("if false for:", false_for_count)
# print("operations:", operations)


def run_algo(n):
    i = 1

    ops = 0

    while i < 2**n:

        if i <= 4 or i >= 2**(n-2):
            j = n
            while j >= 0:
                j -= 2
                ops += 1
        else:
            j = n
            while j > 1:
                j = math.ceil(j/2)
                ops += 1

        i *= 2

    print("----------------------------")
    expected_ops = (n-5) * math.ceil(math.log(n, 2)) + 5*(math.floor(n / 2) + 1)
    print("n:", n)
    print("Expected operations: ", expected_ops)
    print("operations:", ops)
    if expected_ops != ops:
        print("FAIL")
        return
    print("----------------------------")


for i in range(5, 200):
    run_algo(i)
