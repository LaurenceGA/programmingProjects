#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "test1.py", "7/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import time
import random
import sys
import string

count = 0
print_str = string.ascii_letters + string.punctuation + string.hexdigits
# print_str = "01 "
str_len = len(print_str)-1


while True:
    # sys.stdout.write(str(random.randint(0, 10)))
    sys.stdout.write(print_str[random.randint(0, str_len)])

    if not count % 5:
        sys.stdout.flush()

    count += 1

    time.sleep(0.001)