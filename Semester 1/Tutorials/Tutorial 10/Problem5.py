#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Problem5.py", "25/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def get_details():
    title = input("Title: ")
    if title.lower() == 'exit':
        return None
    cost = input("Cost: ")

    new_dict = {
        'title': title,
        'cost': cost
    }

    return new_dict

item = {}
items = []

while item is not None:
    if item is not None:
        item = get_details()
        items.append(item)

for i in items:
    print(i)