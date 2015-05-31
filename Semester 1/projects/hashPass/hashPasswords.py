__author__ = 'Laurence Armstrong'
print("%s created on %s by %s (%d)\n%s\n" % ("hashPasswords.py", "2/04/15", __author__, 15062061, "-----" * 15))

import hashlib
import string
from time import clock

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

def crack_pass(hsh):
    from time import time
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + ";:"
    # chars = string.ascii_letters
    # chars = string.digits

    for i in range(1, 10):
        checkChar(hsh, chars, i, "")

crack_pass(get_hexhash("heyy"))