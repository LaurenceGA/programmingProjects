#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Problem2.py", "25/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

item = {'title': 'Toaster', 'cost': '79.95', 'brand': 'Vogels'}

items = ""

for key, value in item.items():
    items += key+': '+value+'\n'

print(items)