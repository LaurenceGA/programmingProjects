#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "spring.py", "15/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import pygame

import constants


class Spring:
    def __init__(self, mass1, mass2, s_const, length):
        self.mass1 = mass1
        self.mass2 = mass2
        self.s_const = s_const  # Spring constant
        self.length = length

        self.colour = constants.BLUE
        self.f_const = 0.2

    def step(self):
        # F = -kx
        dist = self.mass1.pos.dist(self.mass2.pos)
        extension = dist - self.length
        # if extension < 0:
        #     extension *= 5
        force = self.mass1.pos.subtract(self.mass2.pos).normalize().scale(extension * self.s_const)

        force = force.add((self.mass1.velocity.subtract(self.mass2.velocity)).scale(self.f_const))

        self.mass1.add_force(force.scale(-1))
        self.mass2.add_force(force)

    def draw(self, screen):
        pygame.draw.line(screen, self.colour, (self.mass1.pos.x, self.mass1.pos.y), (self.mass2.pos.x, self.mass2.pos.y), 5)