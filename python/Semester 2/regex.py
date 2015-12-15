#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "regex.py", "29/10/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re

OPERATOR = r"([\+\-/\*\^])"
NUMBER = r"(\d*\.?\d+)"
VARIABLE = r"([a-zA-Z]{1})"

NUMORVAR = "(" + NUMBER + "|" + VARIABLE + ")"
SPACE = r"(\s+)"
OPTSPACE = r"(\s*)"

PREFIX = OPERATOR + SPACE + NUMORVAR + SPACE + NUMORVAR
INFIX = NUMORVAR + OPTSPACE + OPERATOR + OPTSPACE + NUMORVAR
POSTFIX = NUMORVAR + SPACE + NUMORVAR + SPACE + OPERATOR

# print re.search(r"([\+\-/\*\^])", ".") is not None
print re.search(OPERATOR, ".") is not None
