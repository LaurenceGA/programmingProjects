#!/usr/bin/env python
from sys import stdout
__author__ = "Laurence Armstrong"
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "constants.py", "3/08/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

FPS = 60

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
