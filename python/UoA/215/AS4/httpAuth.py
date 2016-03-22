#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "httpAuth.py", "22/03/2016", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import base64
import hashlib

usr = "379831272"
psswd = "272138973"


def encode64(u, p):
    comb = u + ":" + p
    # comb = "s"
    bin_str = ""
    for c in comb:
        bin_str += format(ord(c), "08b")
    bin_str += "0" * (6-(len(bin_str) % 6))

    i = 1
    for b in bin_str:
        print(b, end="")
        if i % 6 == 0:
            print(" ", end="")
        i += 1

    return bin_str

# a = encode64(usr, psswd)
a = base64.b64encode(bytes(usr + ":" + psswd, "utf-8")).decode()
# a = base64.b64encode(bytes("bo", "utf-8")).decode()
# print(a)
# print(base64.b64decode("Z2duYWk6cm9wYQ==").decode())

m = hashlib.md5()
# ha1 = usrnm, realm, psswd
# ha2 = method, uri
# ha1, nonce, ha2
txt = ""
m.update(bytes(txt, "utf-8"))
print(m.hexdigest())
