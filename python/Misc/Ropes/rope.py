#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "rope.py", "15/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from PointMass import PointMass
from spring import Spring

import random


class Rope:
    def __init__(self, x, y, length, sections, s_const):
        sec_length = length / sections
        self.masses = [PointMass(x, y, 1, True)]
        self.springs = []
        cur_y = y
        for mass in range(sections):
            cur_y += sec_length + random.randint(-200, 200)
            self.masses.append(PointMass(x + random.randint(-200, 200), cur_y, 1))

        for spring in range(sections):
            self.springs.append(Spring(self.masses[spring], self.masses[spring+1], s_const, sec_length))

    def step(self):
        for mass in self.masses:
            mass.step()
        for spring in self.springs:
            spring.step()

    def draw(self, screen):
        for mass in self.masses:
            mass.draw(screen)
        for spring in self.springs:
            spring.draw(screen)