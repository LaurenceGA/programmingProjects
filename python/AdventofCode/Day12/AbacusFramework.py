#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "AbacusFramework.py", "14/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import json

f = open('inp.json')
jinp = f.read()
f.close()

jsn = json.loads(jinp)


def sum_json(js):
    if type(js) == dict:
        if 'red' in js.values():
            return 0
        sm = 0
        for i in js.values():
            sm += sum_json(i)
        return sm
    elif type(js) == list:
        sm = 0
        for i in js:
            sm += sum_json(i)
        return sm
    elif type(js) == int:
        return js
    else:
        return 0

print(sum_json(jsn))
