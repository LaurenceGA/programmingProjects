#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "d20.py", "20/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

input_num = 34000000

import itertools

# houses = {}
# for i in range(1, int(input_num/10)):
#     for j in range(i, int(input_num/10), i):
#         houses[j] = houses.get(j, 0) + i*11
#
# house_list = sorted(houses.items(), key=lambda x: x[0])
#
# for i in house_list:
#     if i[1] >= input_num:
#         print(i[0])
#         break
#
#
# def num_presents(h_num):
#     presents = 0
#     for i in range(h_num, 0, -1):
#         if h_num % i == 0:
#             presents += i
#     return presents


a = [13, 5, 4, 4,  3]
p = [ 2, 3, 5, 7, 11]

def f(x):
    t = 1
    for k, j in zip(x, p):
        t *= j ** k
    return t

m = 1e100
mi = None
for i in itertools.product(*[range(i) for i in a]):
    su = 0
    n = f(i)
    for j in itertools.product(*[range(k + 1) for k in i]):
        t = f(j)
        if n // t <= 50:
            su += t
    if su * 11 >= input_num and n < m:
        m = n
        mi = i
print(m, mi)