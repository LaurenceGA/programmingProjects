#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "inputHandler.py", "25/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import pygame


class InputHandler:
    move_left = False
    move_right = False
    move_up = False
    move_down = False

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.move_left = True

                elif event.key == pygame.K_d:
                    self.move_right = True

                elif event.key == pygame.K_w:
                    self.move_up = True

                elif event.key == pygame.K_s:
                    self.move_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.move_left = False

                elif event.key == pygame.K_d:
                    self.move_right = False

                elif event.key == pygame.K_w:
                    self.move_up = False

                elif event.key == pygame.K_s:
                    self.move_down = False

    def __str__(self):
        return "Left: {}, Right: {}, Up: {}, Down: {}".format(self.move_left,
                                                              self.move_right,
                                                              self.move_up,
                                                              self.move_down)