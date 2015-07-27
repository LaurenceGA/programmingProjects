#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "game.py", "25/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import pygame
import random

import gameObject as gameObject
import inputHandler as inp
import fish as fish
from constants import *


class Game:
    spawn_time = 1000
    spawn_timer = 0

    def __init__(self, game_font):
        self.input_handler = inp.InputHandler()
        self.clock = pygame.time.Clock()
        self.instance_list = gameObject.InstanceList(self, game_font)
        self.font = game_font

        self.instance_list.instantiate(fish.Player(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        for i in range(50):
            self.instance_list.instantiate(fish.OtherFish((random.random()-0.5)*100 + random.choice([100, WINDOW_WIDTH-100]),
                                                          random.randrange(100, WINDOW_HEIGHT-100)))
    def game_step(self):
        self.spawn_timer -= self.clock.get_time()
        if self.spawn_timer <= 0:
            self.spawn_timer = self.spawn_time
            self.instance_list.instantiate(fish.OtherFish((random.random()-0.5)*100 + random.choice([100, WINDOW_WIDTH-100]),
                                                          random.randrange(100, WINDOW_HEIGHT-100)))