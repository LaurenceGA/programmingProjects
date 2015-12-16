#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "sim.py", "14/12/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

from NeuralNetwork import NeuralNetwork

import random
import pygame
from math import sin, cos, radians


class Simulation(object):
    def __init__(self, pop, screen, clock):
        self.screen = screen
        self.clock = clock

        self.fish = pop
        self.food = []
        for i in range(len(pop)//2):
            self.spawn_food()

    def spawn_food(self):
        self.food.append(Food([self.screen.get_width()*random.random(), self.screen.get_height()*random.random()],
                              self.screen, self.clock, [self]))

    def step(self):
        for i in self.food + self.fish:
            i.step()

    def draw(self):
        for i in self.food + self.fish:
            i.draw()


def sq_dist(pos1, pos2):
    return (pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2


class Fish(object):
    def __init__(self, pos, screen, clock, sim):
        self.pos = pos
        self.brain = NeuralNetwork(2, 1, 1, 3)
        self.direction = 0
        self.radius = 10
        self.speed = 10

        self.fitness = 0

        self.screen = screen
        self.clock = clock
        self.sim = sim

    def code(self):
        return self.brain.gcode

    def step(self):
        self.pos[0] += self.speed*cos(radians(self.direction)) * self.clock.get_time() / 1000
        self.pos[1] -= self.speed*sin(radians(self.direction)) * self.clock.get_time() / 1000

        nearest_food_pos = self.sim[0].food[0].pos
        cur_dist = sq_dist(self.pos, nearest_food_pos)
        inst = self.sim[0].food[0]
        for fd in self.sim[0].food:
            f_dist = sq_dist(self.pos, fd.pos)
            if cur_dist > f_dist:
                nearest_food_pos = fd.pos
                cur_dist = f_dist
                inst = fd

        relative_pos = ((nearest_food_pos[0] - self.pos[0])/3, (nearest_food_pos[1] - self.pos[1])/3)
        self.direction = self.brain.process(*relative_pos)*360

        margin = inst.radius + self.radius
        if abs(relative_pos[0]) < margin and abs(relative_pos[1]) < margin:
            self.fitness += 1
            del self.sim[0].food[self.sim[0].food.index(inst)]
            self.sim[0].spawn_food()

        # self.direction += 90 * self.clock.get_time() / 1000

    def draw(self):
        pygame.draw.circle(self.screen, (0, 255, 0), (int(self.pos[0]), int(self.pos[1])), self.radius)
        pygame.draw.line(self.screen, (255, 0, 0), (int(self.pos[0]), int(self.pos[1])),
                         (int(self.pos[0]) + self.radius*cos(radians(self.direction)),
                          int(self.pos[1]) - self.radius*sin(radians(self.direction))))


class Food(object):
    def __init__(self, pos, screen, clock, sim):
        self.pos = pos
        self.radius = 5

        self.screen = screen
        self.clock = clock
        self.sim = sim

    def step(self):
        pass

    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 255), (int(self.pos[0]), int(self.pos[1])), self.radius)