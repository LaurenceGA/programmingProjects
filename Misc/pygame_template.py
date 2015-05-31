#!/usr/bin/env python3

import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 960)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # --- Drawing code should go here
    screen.fill(WHITE)

    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)


    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, math.pi / 2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], math.pi / 2, math.pi, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], math.pi, 3 * math.pi / 2, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * math.pi / 2, 2 * math.pi, 2)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("My text", True, BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()