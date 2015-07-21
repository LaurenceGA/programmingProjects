#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "test.py", "14/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print authorship_string,

import pygame
import os

# Centre window
os.environ["SDL_VIDEO_CENTERED"] = "1"
# Initialise
pygame.init()

# Select the font to use, size, bold, italics
gameFont = pygame.font.SysFont('tlwgtypewriter', 25, False, False)

# Set the width, height and position of the screen
screen_size = (1280, 960)
screenInfo = pygame.display.Info()
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("My game!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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


    # First, clear the screen to black
    # --- Drawing code --- #
    screen.fill((0, 0, 0))

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()