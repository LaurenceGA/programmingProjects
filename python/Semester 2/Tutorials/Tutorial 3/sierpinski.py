import pygame
 
# a function that will draw a right-angled triangle of a given size anchored at a given location
def draw_triangle(screen, x, y, size):
    pygame.draw.polygon(screen, white, [[x, y], [x+size, y], [x, y-size]])

############################################################################################# 
# Define a function that will draw Sierpinski's Triangle at a given size anchored at a given location
# You need to update this function 
# currently only one triangle is drawn

def sierpinski(screen, x, y, size):
    # draw_triangle(screen, x, y, size)
    if size > 64:
        pygame.draw.polygon(screen, black, [[x, y], [x+size*2, y], [x, y-size*2]])

        draw_triangle(screen, x, y, size)
        sierpinski(screen, x, y, size*0.5)

        draw_triangle(screen, x, y - size, size)
        sierpinski(screen, x, y - size, size*0.5)

        draw_triangle(screen, x + size, y, size)
        sierpinski(screen, x + size, y, size*0.5)
    else:
        draw_triangle(screen, x, y, size)
        
############################################################################################# 
        
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = [0, 0, 0]
white = [255, 255, 255]
blue = [0, 0, 255]
green = [0, 255, 0]
red = [255, 0, 0]

# Set the height and width of the screen
size = [512, 512]
screen = pygame.display.set_mode(size)
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True    # Flag that we are done so we exit this loop
 
    # Clear the screen and set the screen background
    screen.fill(black)
     
    # Draw Sierpinski's triangle at a given size anchored at a given location

    sierpinski(screen, 0, 512, 512)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Tidy up
pygame.quit()
