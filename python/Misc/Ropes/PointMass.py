#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "PointMass.py", "15/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import constants
from vector import Vector

import pygame


class PointMass():
    def __init__(self, x, y, mass, fixed=False):
        self.pos = Vector(x, y)
        self.mass = mass

        self.colour = constants.BLACK

        self.velocity = Vector()
        self.force = Vector()
        self.angular_velocity = 0

        self.fixed = fixed
        self.selected = False

    def add_gravity(self):
        self.force.y += constants.GRAVITY * self.mass

    def add_force(self, force_vector):
        # print(force_vector)
        self.force = self.force.add(force_vector)

    def accelerate(self):
        self.velocity = self.velocity.add(self.force.scale(1 / self.mass))

    def move(self):
        self.pos = self.pos.add(self.velocity)

    def step(self):
        if not self.fixed:
            # Forces
            self.add_gravity()

            # Velocity
            self.accelerate()
            self.move()

            self.force.reset()

            m_pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                if (m_pos[0] - self.pos.x)**2 + (m_pos[1] - self.pos.y)**2 < (self.mass*30)**2:
                    self.selected = True

            if not pressed[0]:
                self.selected = False

            if self.selected:
                self.add_force(Vector(m_pos[0], m_pos[1]).subtract(self.pos).normalize().scale(1))


    def draw(self, screen):
        m_pos = pygame.mouse.get_pos()
        if (m_pos[0] - self.pos.x)**2 + (m_pos[1] - self.pos.y)**2 < (self.mass*30)**2:
            pygame.draw.circle(screen, self.colour, (round(self.pos.x), round(self.pos.y)), round(self.mass*10))

        # Force and velocity vectors
        # Force
        # pygame.draw.line(screen, constants.RED, (round(self.pos.x), round(self.pos.y)), (self.pos.x + self.force.x, self.pos.y + self.force.y))