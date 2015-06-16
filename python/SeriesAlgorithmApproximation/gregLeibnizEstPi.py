#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "gregLeibnizEstPi.py", "5/06/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from time import clock

# 4 * SUM <((-1)^(n+1))/(2n - 1)>
def lieb_nth(n):
    return ((-1)**n)/((2*n) + 1)


def lieb(degree):
    current = 0

    for n in range(0, degree):
        current += lieb_nth(n)

    return 4 * current

start = clock()
pi = lieb(50000000)
time = clock() - start
print(pi)
print("Done in {} seconds".format(time))


# 3.1415926 5359
#          ^50 million iterations of series in 36.2 seconds
