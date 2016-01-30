#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "d23.py", "23/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re

instructions = [line.rstrip() for line in open('inp.txt')]

registers = {
    'a': 1,
    'b': 0
}

i_index = 0

while 0 <= i_index < len(instructions):
    instruction = instructions[i_index]
    m = re.match(R'(\w{3})\s((?:[ab],?)|(?:[\+\-]\d+))(?:\s([\+\-]\d+))?', instruction)
    if m:
        func = m.group(1)
        arg1 = m.group(2).replace(',', '')
        arg2 = m.group(3)
        if func == 'hlf':
            registers[arg1] /= 2
        elif func == 'tpl':
            registers[arg1] *= 3
        elif func == 'inc':
            registers[arg1] += 1
        elif func == 'jmp':
            val = int(arg1)
            i_index += val
            continue
        elif func == 'jie':
            if registers[arg1] % 2 == 0:
                val = int(arg2)
                i_index += val
            else:
                i_index += 1
            continue
        elif func == 'jio':
            if registers[arg1] == 1:
                val = int(arg2)
                i_index += val
            else:
                i_index += 1
            continue
    else:
        print("FAILURE")
    i_index += 1

print("Register a: {}, Register b: {}".format(registers['a'], registers['b']))
