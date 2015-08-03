#!/usr/bin/env python
from sys import stdout
__author__ = "Laurence Armstrong"
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "main.py.py", "3/08/2015", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


import constants as const

import pygame
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

size = (const.WINDOW_WIDTH, const.WINDOW_HEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Geo Wars")

running = True

clock = pygame.time.Clock()

while running:
    # -------- Game logic ----------- #
    # game_instance.step()

    # -------- Draw ----------- #
    screen.fill(const.BLACK)

    # game_instance.draw(screen)

    pygame.display.flip()

    clock.tick(const.FPS)

pygame.quit()
