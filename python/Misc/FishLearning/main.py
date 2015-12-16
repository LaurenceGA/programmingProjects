#!/usr/bin/env python
from sys import stdout
__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "main.py", "6/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


import pygame
import os
import random
import copy

from Fish import Fish
from Food import Food

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

pygame.display.set_caption("Fish!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

oid = 0
instances = []
to_delete = []


def make_generation(fish=None):
    global oid, instances
    if fish:
        networks = [copy.deepcopy(x.network) for x in fish]
    instances = [x for x in instances if isinstance(x, Food)]
    if not fish:
        for i in range(80):
            instances.append(Fish(clock, screen, instances, to_delete, oid))
            oid += 1
    else:
        for i in range(80):
            instances.append(Fish(clock, screen, instances, to_delete, oid, networks[i % 35]))
            oid += 1

    for i in range(200):
        instances.append(Food(screen_size[0] * random.random(), screen_size[1] * random.random(), screen, oid))
        oid += 1

make_generation()


time_elapsed = 0
generation = 1
time_per_generation = 10000

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
    for i in instances:
        i.update()
    # print(to_delete)
    instances = [x for x in instances if x.id not in to_delete]
    to_delete.clear()

    if time_elapsed - generation*time_per_generation > 0:
        fish = [x for x in instances if isinstance(x, Fish)]
        sorted(fish, key=lambda x: x.fitness, reverse=False)
        total = 0
        for f in fish:
            total += f.fitness
        fittest = max(fish, key=lambda x: x.fitness)
        print("Gen: {}, Top Fitness: {}, Average: {}".format(generation, fittest.fitness, total/len(fish)))

        fish[len(fish)//2:] = []

        make_generation(fish)

        generation += 1

    # First, clear the screen to black
    # --- Drawing code --- #
    screen.fill((255, 255, 255))

    for i in instances:
        i.draw()

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)
    time_elapsed += clock.get_time()

# Close the window and quit.
pygame.quit()
