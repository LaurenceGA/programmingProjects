#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "AllInOneNight.py", "14/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re, random
import itertools

info = [line.rstrip() for line in open('inp.txt')]
places = {}


class Place(object):
    def __init__(self):
        self.dist_to = {}

    def __str__(self):
        return str(self.dist_to)

for data in info:
    dist = re.match(R'(.+) to (.+) = (\d+)', data)

    if dist.group(1) not in places:
        places[dist.group(1)] = Place()
    if dist.group(2) not in places:
        places[dist.group(2)] = Place()

    places[dist.group(1)].dist_to[dist.group(2)] = int(dist.group(3))
    places[dist.group(2)].dist_to[dist.group(1)] = int(dist.group(3))

# for k, v in places.items():
#     print(k, v)


def get_dist(order, places):
    dist = 0
    for i in range(len(order)-1):
        dist += places[order[i]].dist_to[order[i+1]]
    return dist


route_dist = []
for i in list(itertools.permutations(places)):
    route_dist.append(get_dist(i, places))

print(max(route_dist))