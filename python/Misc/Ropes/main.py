#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "main.py", "15/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print authorship_string,

import pygame
import os

import constants
# from PointMass import PointMass
# from spring import Spring
from rope import Rope

# Centre window
os.environ["SDL_VIDEO_CENTERED"] = "1"
# Initialise
pygame.init()

# Select the font to use, size, bold, italics
gameFont = pygame.font.SysFont('tlwgtypewriter', 25, False, False)

# Set the width, height and position of the screen
screen_size = (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
screenInfo = pygame.display.Info()
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Ropes!!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


instances = [
    Rope(200, 50, 300, 15, 0.1),
    Rope(400, 50, 300, 15, 0.1)
]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:   # If user clicked close
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            done = True

    # --- Game logic --- #
    # from random import randint
    # instances.append(PointMass(randint(100, 1200), 100, 1))
    for inst in instances:
        inst.step()

    # First, clear the screen
    # --- Drawing code --- #
    screen.fill(constants.WHITE)
    for inst in instances:
        inst.draw(screen)

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to set frames per second
    clock.tick(constants.FPS)

# Close the window and quit.
pygame.quit()