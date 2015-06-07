#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "arctanEstPi.py", "5/06/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from time import clock

# 4 * SUM <((-1)^(n+1))/(2n - 1)>
def arctan_nth(n):
    return ((-1)**(n+1))/((2*n) - 1)


def mc_arctan(degree):
    current = 0

    for n in range(1, degree):
        current += arctan_nth(n)

    return 4 * current

start = clock()
pi = mc_arctan(25000000)
time = clock() - start
print(pi)
print("Done in {} seconds".format(time))


# 3.1415926 5359
#          ^25 million iterations of series in 18.5 seconds
