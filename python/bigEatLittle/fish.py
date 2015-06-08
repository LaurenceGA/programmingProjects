#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "fish.py", "25/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from bigEatLittle.gameObject import Object
from bigEatLittle.constants import *
from bigEatLittle.spriteSheet import SpriteSheet

import pygame
import random


class Fish(Object):
    alive = True
    move_speed = 5
    size = 0.3

    def __init__(self, x=0, y=0):
        self.x_scale = self.size
        self.y_scale = self.size
        super().__init__(x, y)

    def wrap_pos(self, x=True, y=True):
        if x:
            if self.x - (self.width * self.x_scale)/2 > WINDOW_WIDTH:
                self.x = -(self.width * self.x_scale)/2
                self.rect.x = -(self.width * self.x_scale)/2
            elif self.x + (self.width * self.x_scale)/2 < -(self.width * self.x_scale)/2:
                self.x = WINDOW_WIDTH + (self.width * self.x_scale)/2
                self.rect.x = WINDOW_WIDTH + (self.width * self.x_scale)/2

        if y:
            if self.y - (self.height * self.y_scale)/2 > WINDOW_HEIGHT:
                self.y = -(self.height * self.y_scale)/2
                self.rect.y = -(self.height * self.y_scale)/2
            elif self.y + (self.height * self.y_scale)/2 < -(self.height * self.y_scale)/2:
                self.y = WINDOW_HEIGHT + (self.height * self.y_scale)/2
                self.rect.y = WINDOW_HEIGHT + (self.height * self.y_scale)/2

    def collide(self, obj):
        if obj is Fish or issubclass(type(obj), Fish):
            self.eat_fish(obj)

    def eat_fish(self, other_fish):
        if self.size > other_fish.size:
            self.scale(other_fish.size/4)
            other_fish.destroy()

    def scale(self, amount):
        self.size += amount
        self.x_scale = self.size
        self.y_scale = self.size
        self.x -= self.width*amount/2
        self.y -= self.height*amount/2
        self.set_rect()

    def step(self):
        super().step()
        self.wrap_pos()


class Player(Fish):
    colour = GREEN

    def step(self):
        if self.game.input_handler.move_left and not self.game.input_handler.move_right and self.alive:
            self.x_speed = -self.move_speed
        elif self.game.input_handler.move_right and not self.game.input_handler.move_left and self.alive:
            self.x_speed = self.move_speed
        else:
            self.x_speed = 0

        if self.game.input_handler.move_up and not self.game.input_handler.move_down and self.alive:
            self.y_speed = -self.move_speed
        elif self.game.input_handler.move_down and not self.game.input_handler.move_up and self.alive:
            self.y_speed = self.move_speed
        else:
            self.y_speed = 0

        super().step()

        self.wrap_pos()


class OtherFish(Fish):
    def __init__(self, x=0, y=0):
        self.size = 0.3 + (random.random()-0.5)/4
        self.x_scale = self.size
        self.y_scale = self.size
        self.y_speed = random.random()/3
        self.x_speed = random.random() - 0.5
        super().__init__(x, y)