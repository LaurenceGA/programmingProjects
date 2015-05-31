__author__ = 'Laurence Armstrong'
print("%s created on %s by %s (%d)\n%s\n" % ("hashPasswords.py", "2/04/15", __author__, 15062061, "-----" * 15))

import hashlib
import string
from time import clock
import os

found = False

def get_hexhash(str):
    return hashlib.sha256(str.encode()).hexdigest()

def checkChar(hsh, chars, number, word):
    global found

    if found:
        return

    if number >= 1:
        for c in chars:
            checkChar(hsh, chars, number - 1, word + c)
    else:
        # testHash = get_hexhash(word)
        # print(word, end="")
        # print("\b" * len(word), end="")
        if hsh == get_hexhash(word):
            print("password is %s in %fseconds" % (word, clock()))
            found = True
            return


def readFile(path):
    file = open(path)
    fileContents = file.read()
    file.close()

    return fileContents

def crack_pass(hsh):
    global found
    chars = string.ascii_lowercase + string.digits# + string.ascii_uppercase + ";:"
    # chars = string.ascii_letters
    # chars = string.digits

    hashList = readFile(os.getcwd() + "/resources/lowdigit").split("\n")

    for i in range(0, len(hashList), 2):
        # print("\b"*len(hashList[i+1]), end="")
        # print(hashList[i+1], end="")
        # print("Testing %s" % hashList[i])
        if hashList[i] == hsh:
            word = hashList[i+1]
            print("password is %s in %fseconds" % (word, clock()))
            found = True
            return

    fileNum = 4

    if not found:
        for i in range(fileNum + 1, 12):
            print("Checking %d letter words" % i)
            checkChar(hsh, chars, i, "")

crack_pass(get_hexhash("1z48"))