#!/usr/bin/env python
from sys import stdout
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "main.py", "7/12/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import pygame
import os

from genAlg import GenAlg

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

pygame.display.set_caption("Neuroevolution!")

# Loop until finished
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

alg = GenAlg(50, screen, clock)

comp_per_draw = 1

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:   # If user clicked close
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                comp_per_draw += 1
            elif event.key == pygame.K_LEFT:
                comp_per_draw = max(comp_per_draw-1, 1)

    for i in range(comp_per_draw):
        alg.update()
    clock.tick()

    # --- Drawing code --- #
    screen.fill((255, 255, 255))
    alg.draw()

    # --- Update the screen
    pygame.display.flip()


# Close the window and quit.
pygame.quit()

# def main():
#     brain = NeuralNetwork(2, 1, 1, 3)
#     brain2 = NeuralNetwork(2, 1, 1, 3, brain.gcode)
#
#     out = brain.process(3, 2)
#     print(out)
#
#     out = brain2.process(3, 2)
#     print(out)
#
# if __name__ == "__main__":
#     main()