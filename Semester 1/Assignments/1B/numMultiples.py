#!/usr/bin/env python
# 159.171 Assignment 1B
# Laurence Armstrong, 15062061
__author__ = 'Laurence Armstrong'
authorship_string = "%s created by %s (%d)\n%s\n" % \
                    ("numMultiples.py", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

def getMultiples(num, limit):
    multiples = []

    for i in range(int(limit/num)):
        multiples.append(num*(i+1))

    return multiples


def getListProduct(numList):
    product = 1
    for num in numList:
        product *= num

    return product


try:
    number = int(input("Enter a number: "))
    limit = int(input("Enter a limit: "))

    mul = getMultiples(number, limit)

    print(mul)
    print("The product of the list is {}".format(getListProduct(mul)))
except ValueError:
    print("That is not an acceptable input.")