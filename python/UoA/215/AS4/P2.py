#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "P2.py", "23/03/16", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import hashlib

username = b"379831272"
realm = b"Mordor"
password = b"272138973"

method = b"GET"
uri = b"/Public/CS/Home.png"

nonce = b"03e2abb8a924e966bee59d41cef32851"

m = hashlib.md5()
m.update(username + b":" + realm + b":" + password)
ha1 = m.digest()
print(m.hexdigest())

m = hashlib.md5()
m.update(method + b":" + uri)
ha2 = m.digest()
print(m.hexdigest())

m = hashlib.md5()
m.update(ha1 + b":" + nonce + b":" + ha2)
response = m.hexdigest()
print(response)

# wordsf = open("/usr/share/dict/american-english")
wordsf = open("words.txt")
words = wordsf.readlines()
wordsf.close()
# words.append("272138973")

response = "04e720da868a0736c4ee3fca55c7a8a8"
for w in words:
    word = w.strip()

    m = hashlib.md5()
    m.update(username + b":" + realm + b":" + bytes(word, "utf-8"))
    ha1 = m.digest()

    m = hashlib.md5()
    m.update(ha1 + b':' + nonce + b':' + ha2)
    resp = m.hexdigest()

    if resp == response:
        print("FOUND: " + word)
        break
