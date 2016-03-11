#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "CaesarCipher.py", "29/02/2016", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


inp = "Bekyi mekbt dej wylu kf jxu Imeht."

for k in range(26):
    decoded_str = ""
    for c in inp:
        lower = c.islower()
        if c.isalpha():
            converted = chr(((ord(c.lower()) - ord('a') + k) % 26) + ord('a'))
            decoded_str += converted.lower() if lower else converted.upper()
        else:
            decoded_str += c
    print("{}:\n{}\n".format(chr(k + ord('a')), decoded_str, '\n'))
