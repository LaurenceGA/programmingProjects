#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "Fish.py", "6/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

from NeuralNetwork.Network import NeuralNetwork

import pygame
import random
import math
import copy

from Food import Food


class Fish(object):
    def __init__(self, clock, screen, instances, to_delete, id, network=None):
        self.clock = clock
        self.screen = screen
        self.instances = instances
        self.to_delete = to_delete
        self.id = id

        self.radius = 7
        self.speed = 3

        self.xpos = random.randint(0, screen.get_width())
        self.ypos = random.randint(0, screen.get_height())

        self.rotation = random.randint(0, 360)

        self.fitness = 0
        self.food = 0
        self.time = 0

        if network:
            self.network = copy.deepcopy(network)
            network.randomise(0.15)
        else:
            self.network = NeuralNetwork(2, 2, 1, 3)

    def dist(self, other):
        return (other.xpos - self.xpos)**2 + (other.ypos - self.ypos)**2

    def update(self):
        self.time += self.clock.get_time()

        food = [x for x in self.instances if isinstance(x, Food)]
        closest_food = min(food, key=lambda x: self.dist(x))

        margin = self.radius + closest_food.radius
        if abs(self.xpos - closest_food.xpos) < margin and abs(self.ypos - closest_food.ypos) < margin and closest_food.id:
            if closest_food.id not in self.to_delete:
                self.food += 1
                self.to_delete.append(closest_food.id)

        # proc_output = self.network.process((closest_food.xpos - self.xpos)/1280,
        #                                    (closest_food.ypos - self.ypos)/960)[0]
        proc_output = self.network.process((closest_food.xpos - self.xpos)/10,
                                           (closest_food.ypos - self.ypos)/10)

        # if self.id == 5:
            # print(((closest_food.xpos - self.xpos)/128, (closest_food.ypos - self.ypos)/96))
            # print(proc_output)

        # self.rotation = 360*proc_output
        self.rotation += proc_output[0]*3
        # print(((closest_food.xpos - self.xpos)/1280, (closest_food.ypos - self.ypos)/960))

        self.xpos += (self.speed * proc_output[1])*math.cos(math.radians(self.rotation))
        self.ypos -= (self.speed * proc_output[1])*math.sin(math.radians(self.rotation))

        if self.time == 0:
            self.fitness = 0
        else:
            # self.fitness = self.food/self.time
            self.fitness = self.food

    def draw(self):
        pygame.draw.circle(self.screen, (0, 255, 0), (int(self.xpos), int(self.ypos)), self.radius)
        pygame.draw.line(self.screen, (255, 0, 0), (self.xpos, self.ypos),
                         (self.xpos + self.radius*math.cos(math.radians(self.rotation)),
                          self.ypos - self.radius*math.sin(math.radians(self.rotation))))

    def __str__(self):
        return "Fish of fitness {} and ({}, {})".format(self.fitness, self.xpos, self.ypos)
