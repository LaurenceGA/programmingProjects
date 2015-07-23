# Import the library of functions called 'pygame'
import pygame


# Define a function that will draw a snowman at a certain location
def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, white, [35+x, 0+y, 25, 25])
    pygame.draw.ellipse(screen, white, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, white, [0+x, 65+y, 100, 100])


def draw_snowman2(screen, x, y, s):
    pygame.draw.ellipse(screen, white, [35*s+x, 0*s+y, 25*s, 25*s])
    pygame.draw.ellipse(screen, white, [23*s+x, 20*s+y, 50*s, 50*s])
    pygame.draw.ellipse(screen, white, [0*s+x, 65*s+y, 100*s, 100*s])


def draw_snowmen(screen, x, y):
    if x + 100 < size[0]:
        draw_snowman(screen, x, y)
        draw_snowmen(screen, x + 100, y)


def draw_snowmen2(screen, x, y, s):
    # if x + (100*s) < size[0]:
    if s > 0.01:     # Snowman is too small
        draw_snowman2(screen, x, y, s)
        draw_snowmen2(screen, x + 100*s, y, s*0.9)

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = [0, 0, 0]
white = [255, 255, 255]
blue = [0, 0, 255]
green = [0, 255, 0]
red = [255, 0, 0]

# Set the height and width of the screen
size = [1050, 500]
screen = pygame.display.set_mode(size)
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:    # If user clicked close
            done = True     # Flag that we are done so we exit this loop
 
    # Clear the screen and set the screen background
    screen.fill(black)
     
    # Draw Snowman at a particular location
    draw_snowmen2(screen, 10, 200, 1)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Tidy up
pygame.quit()
