#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "ReindeerRace.py", "14/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re

race_time = 2503

stats = [line.rstrip() for line in open('inp.txt')]


class Reindeer(object):
    def __init__(self, name, top_speed, fly_time, rest_time):
        self.name = name
        self.top_speed = top_speed
        self.fly_time = fly_time
        self.rest_time = rest_time

        self.flying = True
        self.dist = 0
        self.time_to_change = fly_time

        self.points = 0

    def step(self):
        if self.time_to_change == 0:
            if self.flying:
                self.time_to_change = self.rest_time
            else:
                self.time_to_change = self.fly_time
            self.flying = not self.flying

        if self.flying:
            self.dist += self.top_speed

        self.time_to_change -= 1

    def __gt__(self, other):
        return self.dist > other.dist

    def __str__(self):
        return "{} is {} at {}m with {} points".format(self.name,
                                                       "flying" if self.flying else "resting",
                                                       self.dist,
                                                       self.points)

deer = []

for r in stats:
    m = re.match(R'(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', r)
    deer.append(Reindeer(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))

for i in range(race_time):
    # if not i % 10:
    #     for d in deer:
    #         print(d)
    #     print()
    for d in deer:
        d.step()

    top = max(deer)
    print(top)
    top = top.dist
    lead_deer = [r for r in deer if r.dist == top]

    for r in lead_deer:
        r.points += 1

print(max(deer, key=lambda x: x.points).points)
