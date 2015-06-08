#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "pyception.py", "12/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import pygame
import os
import sys
import string
import io

screen_size = (1280, 960)
KEY_REPEAT_SETTING = (200, 70)
ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pyception")
clock = pygame.time.Clock()
pygame.key.set_repeat(*KEY_REPEAT_SETTING)

done = False


def new_linify(string):
    return string.replace('\\n', '\n')

class UiBox:
    def __init__(self, x, y, width, height, fill=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill_colour = (0, 0, 0)
        self.border_colour = (255, 255, 255)
        self.fill = fill

    def handle_input(self, event):
        pass

    def draw(self, screen):
        # Inner fill
        if self.fill:
            pygame.draw.rect(screen, self.fill_colour, [self.x, self.y, self.width, self.height], 0)
        # Border
        pygame.draw.rect(screen, self.border_colour, [self.x, self.y, self.width, self.height], 1)


class TextBox(UiBox):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.buffer = []
        self.font = pygame.font.Font(None, 36)
        self.font_colour = (255, 255, 255)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.buffer.append('\n')
            elif event.key == pygame.K_BACKSPACE:
                if self.buffer:
                    self.buffer.pop()
            elif event.key == pygame.K_TAB:
                self.buffer.append("    ")
            elif event.unicode in ACCEPTED:
                self.buffer.append(event.unicode)
        # elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        #     self.active = self.rect.collidepoint(event.pos)

    def draw(self, screen):
        super().draw(screen)
        text = "".join(self.buffer)
        txt = self.font.render(text, True, self.font_colour)
        t_size = self.font.size(text)
        screen.blit(txt, [self.x + 10, self.y + 10])


class OutputBox(UiBox):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.text = io.StringIO()
        self.font = pygame.font.Font(None, 36)
        self.font_colour = (255, 255, 255)

    def draw(self, screen):
        super().draw(screen)
        txt = self.font.render(self.text.getvalue(), True, self.font_colour)
        t_size = self.font.size(self.text.getvalue())
        screen.blit(txt, [self.x + 5, self.y + 5])


class Button(UiBox):
    def __init__(self, x, y, width, height, text, code):
        super().__init__(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, self.height+4)
        self.font_colour = (255, 255, 255)
        self.code = code

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pos_in(*pygame.mouse.get_pos()):
                sys.stdout.truncate(0)
                sys.stdout.seek(0)
                try:
                    exec("".join(self.code))
                except Exception as e:
                    print("That is not correct!", e)

    def pos_in(self, x, y):
        if self.x <= x <= self.x + self.width \
                and self.y <= y <= self.y + self.height:
            return True
        return False

    def draw(self, screen):
        super().draw(screen)
        txt = self.font.render(self.text, True, self.font_colour)
        t_size = self.font.size(self.text)
        screen.blit(txt, [self.x + self.width/2 - t_size[0]/2, self.y + self.height/2 - t_size[1]/2])


def event_loop():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            done = True
        else:
            for box in boxes:
                box.handle_input(event)

main_box_size = (800, 400)
main_box_height = 100
button_size = (80, 40)
output_size = (800, 250)

t_box = TextBox(screen_size[0]/2 - main_box_size[0]/2,
                main_box_height,
                main_box_size[0],
                main_box_size[1])

out_box = OutputBox(screen_size[0]/2 - output_size[0]/2,
                    main_box_height + main_box_size[1] + output_size[1]/2,
                    output_size[0],
                    output_size[1])

sys.stdout = out_box.text

boxes = [
    t_box,
    Button(screen_size[0]/2 + main_box_size[0]/2 - button_size[0],
           main_box_height + main_box_size[1] + 10,
           button_size[0],
           button_size[1],
           "Run",
           t_box.buffer),
    out_box
]

while not done:
    # event
    event_loop()

    # update

    # render
    screen.fill((0, 0, 0))

    for box in boxes:
        box.draw(screen)

    pygame.display.flip()
    clock.tick(60)

out_box.text.close()