#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "SphereHouse.py", "13/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


real_coords = [0, 0]
robo_coords = [0, 0]
present_locations = [tuple(real_coords), tuple(robo_coords)]

f = open('inp.txt')
instructions = f.read()
f.close()

coords = real_coords

for i in instructions:
    if i == '>':
        coords[0] += 1
    elif i == '<':
        coords[0] -= 1
    elif i == '^':
        coords[1] += 1
    elif i == 'v':
        coords[1] -= 1
    else:
        print("ERROR!!")
    present_locations.append(tuple(coords))
    if coords is real_coords:
        coords = robo_coords
    else:
        coords = real_coords

print("Number of houses: {}".format(len(set(present_locations))))
