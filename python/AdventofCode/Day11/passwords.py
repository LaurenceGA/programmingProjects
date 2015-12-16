#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "passwords.py", "14/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

inp = 'hepxcrrq'
# inp = 'hepxxzaa'  # Next


def incriment(cur, pos=-1):
    if pos == -len(cur) - 1:
        raise ValueError("No more")

    if cur[pos] == 'z':
        ls = list(cur)
        ls[pos] = 'a'
        return incriment(''.join(ls), pos-1)
    elif cur[pos] in ['i', 'o', 'l']:
        ls = list(cur)
        ls[pos] = chr(ord(ls[pos])+2)
        return ''.join(ls)
    else:
        ls = list(cur)
        ls[pos] = chr(ord(ls[pos])+1)
        return ''.join(ls)

c = 0

satisfied = False
while not satisfied:
    has_triple = False
    if 'i' in inp or 'o' in inp or 'l' in inp:
        inp = incriment(inp)
        continue

    double_letters = 0
    counted = False
    for i, ch in enumerate(inp):
        if counted:
            counted = False
            continue

        if i < len(inp) - 1:
            if ch == inp[i+1]:
                double_letters += 1
                counted = True

    for i, ch in enumerate(inp):
        if i < len(inp) - 2:
            if chr(ord(ch)+1) == inp[i+1] and chr(ord(ch)+2) == inp[i+2]:
                has_triple = True

    if has_triple and double_letters >= 2:
        satisfied = True
    else:
        inp = incriment(inp)

    c += 1
    if c % 50000 == 0:
        print(inp)

print("\nPassword is {} after {} iterations".format(inp, c))
