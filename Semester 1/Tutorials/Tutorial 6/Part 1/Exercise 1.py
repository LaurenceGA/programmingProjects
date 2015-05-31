#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" % \
                    ("Exercise 1.py", "20/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

def print_alternates(limit, word1, word2):
    for i in range(limit):
        if (i+1) % 2:
            print(word1)    # Odd
        else:
            print(word2)    # Even

try:
    lim = int(input("Enter a limit:"))

    print_alternates(lim, 'Red', 'Gold')

except ValueError:
    print("Nope")