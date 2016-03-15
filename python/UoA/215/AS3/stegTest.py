#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "stegTest.py", "14/03/16", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

code = """\
(95,153,55) (152,219,165) (78,168,16) (71,115,158) (129,102,218)
(221,14,237) (179,96,186) (56,210,124) (85,93,125) (210,214,6)
(90,105,68) (21,89,18) (89,226,245) (88,66,51) (149,80,224)
(91,50,210) (19,7,103) (18,209,159) (148,26,177) (143,171,120)
(124,53,17) (233,10,20) (161,55,30) (70,30,209) (16,234,203)
(208,73,117) (47,145,38) (170,249,65) (106,173,69) (159,61,147)
(185,189,155) (195,208,104) (82,225,162) (121,130,146) (109,146,251)"""

code = code.split('\n')

lsbs = []

for line in code:
    tuples = line.split()
    for t in tuples:
        px = t[1:len(t)-1].split(',')
        for comp in px:
            lsbs.append(int(comp) & 1)

read_pos = 0
tx_len = 0

tx_len |= lsbs[read_pos]
read_pos += 1
tx_len <<= 1

tx_len |= lsbs[read_pos]
read_pos += 1
tx_len <<= 1

tx_len |= lsbs[read_pos]
read_pos += 1
tx_len <<= 1

tx_len |= lsbs[read_pos]
read_pos += 1

tx_len = int(bin(tx_len)[:1:-1], 2)

chars = []
for j in range(tx_len):
    char = []

    for i in range(8):
        char.insert(0, str(lsbs[read_pos]))
        read_pos += 1

    char = int("".join(char), 2)
    chars.append(chr(char))

for c in chars:
    print(c, end="")
print()
