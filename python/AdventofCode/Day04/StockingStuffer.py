#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "StockingStuffer.py", "13/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import hashlib

inp = 'bgvyzdsv'

answer = 1

hsh = hashlib.md5()

hsh.update((inp + str(answer)).encode())

while hsh.hexdigest()[:6] != '000000':
    answer += 1
    hsh = hashlib.md5()
    hsh.update((inp + str(answer)).encode())

print(answer)
hsh = hashlib.md5()
hsh.update((inp + str(answer)).encode())
print(hsh.hexdigest())
