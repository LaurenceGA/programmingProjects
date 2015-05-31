#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" % \
                    ("Exercise 2.py", "20/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

sum = 0
pos = 0
zeroes = 0
neg = 0

for i in range(7):
    try:
        num = int(input("Enter a number: "))
        sum += num

        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zeroes += 1
    except ValueError:
        print("Nope")

print("sum: %d" % sum)
print("Positives: %d, Negatives: %d, Zeros: %d" % (pos, neg, zeroes))