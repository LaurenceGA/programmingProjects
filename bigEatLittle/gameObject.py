#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "gameObject.py", "25/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import pygame

from bigEatLittle.constants import *


class InstanceList:
    def __init__(self, game, font):
        self.instances = []
        self.game = game
        # self.input_handler = game.input_handler
        # self.clock = game.clock
        # self.font = font

    def logic(self):
        for instance in self.instances:
            instance.step()

    def render(self, screen):
        for instance in self.instances:
            instance.draw(screen)

    def instantiate(self, obj):
        # obj.instance_handler = self
        # obj.input_handler = self.input_handler
        # obj.clock = self.clock
        obj.game = self.game
        self.instances.append(obj)
        obj.awake()
        return obj

    def remove(self, inst):
        for instance in self.instances:
            if instance == inst:
                del self.instances[self.instances.index(instance)]

    def find_of_type(self, typ):
        insts_of_type = []
        for instance in self.instances:
            if instance is typ or issubclass(type(instance), typ):
                insts_of_type.append(instance)
        return insts_of_type

    def find_first_of_type(self, typ):
        for instance in self.instances:
            if instance is typ or issubclass(type(instance), typ):
                return instance
        return None

    def remove_of_type(self, typ):
        insts = self.find_of_type(typ)
        for inst in insts:
            inst.destroy()

    def __str__(self):
        string = ""
        for instance in self.instances:
            string += str(instance) + ", "
        return string


class Object:
    # Object base width
    width = 70
    height = 32

    solid = False

    x_scale = 1
    y_scale = 1

    x_speed = 0
    y_speed = 0

    game = None

    frames = 2

    animation = []
    sprite_sheet = None
    sprite_origin = (0, 0)
    sprite_dimensions = (1, 1)
    image_index = 0
    image = None
    colour = WHITE

    def __init__(self, x=0, y=0, ):
        self.x = x
        self.y = y

        # Collision rectangle
        self.rect = pygame.Rect(self.x, self.y, self.width * self.x_scale, self.height * self.y_scale)

        if self.sprite_sheet:
            self.width = self.sprite_dimensions[0]
            self.height = self.sprite_dimensions[1]
            self.load_sprites()

    def load_sprites(self):
        img = []
        for i in range(self.frames):
            image = self.sprite_sheet.get_image(self.sprite_origin[0] + self.sprite_dimensions[0]*i,
                                                self.sprite_origin[1],
                                                self.sprite_dimensions[0],
                                                self.sprite_dimensions[1])
            image = pygame.transform.scale(image, (round(self.width * self.x_scale), round(self.height * self.y_scale)))
            img.append(image)

        self.animation = img
        self.image = self.animation[self.image_index]

    def awake(self):
        pass

    def set_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width * self.x_scale, self.height * self.y_scale)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.set_rect()

    def animate(self):
        self.image_index += 1
        self.image = self.animation[self.image_index % 2]

    def get_collisions(self):
        for obj in self.game.instance_list.instances:
            if obj is not self:
                if self.rect.colliderect(obj.rect):
                    self.collide(obj)

    def collide(self, obj):
        pass

    def step(self):
        self.get_collisions()
        self.move()

        # self.animate()

    def draw(self, screen):
        if self.sprite_sheet:
            self.image = pygame.transform.scale(self, (round(self.width * self.x_scale), round(self.height * self.y_scale)))
            screen.blit(self.image, [self.x - self.width/2, self.y - self.height/2])
        else:
            pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width * self.x_scale, self.height * self.y_scale])

        # Draw collider
        # pygame.draw.rect(screen, BLUE, self.rect, 1)

    def destroy(self):
        self.game.instance_list.remove(self)