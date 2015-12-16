#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "ChristmasLights.py", "13/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re

light_gid = [[0 for i in range(1000)] for j in range(1000)]

instructions = [line.rstrip() for line in open('inp.txt')]


def change_lights(lights, start, end, ammount):
    # Where typ is True, False or None
    for y in range((end[1] - start[1]) + 1):
        for x in range((end[0] - start[0]) + 1):
            lights[start[0] + x][start[1] + y] = max(lights[start[0] + x][start[1] + y] + ammount, 0)


for i in instructions:
    # break
    if "turn off" in i:
        data = re.match(R'turn off (.*),(.*) through (.*),(.*)', i)
        change_lights(light_gid,
                      (int(data.group(1)), int(data.group(2))),
                      (int(data.group(3)), int(data.group(4))),
                      -1)
    elif "turn on" in i:
        data = re.match(R'turn on (.*),(.*) through (.*),(.*)', i)
        change_lights(light_gid,
                      (int(data.group(1)), int(data.group(2))),
                      (int(data.group(3)), int(data.group(4))),
                      1)
    elif "toggle" in i:
        data = re.match(R'toggle (.*),(.*) through (.*),(.*)', i)
        change_lights(light_gid,
                      (int(data.group(1)), int(data.group(2))),
                      (int(data.group(3)), int(data.group(4))),
                      2)
    else:
        print("PANIC")

total = 0
for x in light_gid:
    total += sum(x)

print(total)
