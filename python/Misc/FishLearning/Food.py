#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "Food.py", "6/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import pygame


class Food(object):
    def __init__(self, xpos, ypos, screen, id):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = 2
        self.id = id

        self.screen = screen

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 255), (int(self.xpos), int(self.ypos)), self.radius)

    def __str__(self):
        return "Food at ({}, {})".format(self.xpos, self.ypos)
