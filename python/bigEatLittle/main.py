#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "main.py", "25/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import pygame
import os

# import bigEatLittle.gameObject as gameObject
# import spaceInvaders.player as player
# import bigEatLittle.inputHandler as inp
import bigEatLittle.constants as const
import bigEatLittle.game as game

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Select the font to use, size, bold, italics
game_font = pygame.font.SysFont('tlwgtypewriter', 25, False, False)

# Set the width, height and position of the screen
size = (const.WINDOW_WIDTH, const.WINDOW_HEIGHT)
screenInfo = pygame.display.Info()

# centre window
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screenInfo.current_w/2 - size[0]/2, screenInfo.current_h/2 - size[1]/2)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Big eats little!")

# Loop until the user clicks the close button.
done = False

game_inst = game.Game(game_font)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:   # If user clicked close
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            done = True
    game_inst.input_handler.handle_input(events)

    # --- Game logic --- #
    game_inst.game_step()
    game_inst.instance_list.logic()

    # First, clear the screen to black
    # --- Drawing code --- #
    screen.fill(const.BLACK)

    game_inst.instance_list.render(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    game_inst.clock.tick(60)

# Close the window and quit.
pygame.quit()