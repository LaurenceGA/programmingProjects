#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Problem 3.py", "18/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

found_count = 0
search_count = 0
names = ["Mary", "Liz", "Miles", "Bob", "Fred"]
numbers = [4, 17, 19]


def find(item):
    global names, numbers, found_count, search_count
    search_count += 1
    for name in names:
        if item == name:
            print("Found in names")
            found_count += 1
            break
    else:
        for number in numbers:
            if item == number:
                print("Found in numbers")
                found_count += 1
                break
        else:
            print("Not found")


def result():
    print("Total searches: {}, Found items: {}, Not found: {}".format(search_count, found_count, search_count - found_count))

find("mary")
find("Mary")
find(0)
find(19)
result()