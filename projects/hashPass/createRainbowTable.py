#!/usr/bin/env python

__author__ = 'Laurence Armstrong'
print("%s created on %s by %s (%d)\n%s\n" % ("createRainbowTable.py", "2/04/15", __author__, 15062061, "-----" * 15))

import hashlib
from time import clock
import string
import os

def readFile(path):
    with open(path) as file:
        fileContents = file.read()
        fileContents

    return ""

def writeFile(path, text):
    with open(path, "a") as file:
        file.write(text + "\n")

def get_hexhash(str):
    return hashlib.sha256(str.encode()).hexdigest()

def addHash(hshList, chars, number, word):
    if number >= 1:
        for c in chars:
            addHash(hshList, chars, number - 1, word + c)
        if number >= 3:
            print("%d chunk completed" % (len(chars)**number))
    else:
        hshList.append(get_hexhash(word))
        hashList.append(word)

filePath = os.getcwd() + "/resources/lowdigit"

dir = os.path.dirname(filePath)
if not os.path.exists(dir):
    os.makedirs(dir, exist_ok=True)
fl = open(filePath, "w")
fl.close()

hashList = []
# chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + ";:"
chars = string.digits + string.ascii_lowercase

for i in range(4):
    addHash(hashList, chars, i+1, "")

print("Hashes added, writing %d items to a file!" % len(hashList))

writeLoad = 100000
for i in range(0, len(hashList), writeLoad):
    writeFile(filePath, "\n".join(hashList[i:i+writeLoad]))
    print("%d entries written from list between" % (writeLoad))

print("Written in %fseconds" % clock())
quit()