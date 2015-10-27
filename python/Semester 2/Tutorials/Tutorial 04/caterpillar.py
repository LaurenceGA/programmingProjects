import pygame
import my_catclass
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
lightblue = (0, 100, 255)
 

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size = [1000, 400]
screen = pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Caterpillar")


# Function to draw background scene
def draw_background():
    screen.fill(black)
    pygame.draw.rect(screen, green, [0, 300, 1000, 100])    # Grass
    pygame.draw.rect(screen, lightblue, [0, 0, 1000, 300])    # Sky
    pygame.draw.ellipse(screen, white, [50, 80, 100, 60])     # cloud
    pygame.draw.ellipse(screen, white, [120, 60, 180, 80])    # cloud
    pygame.draw.ellipse(screen, white, [700, 80, 150, 60])    # cloud
    
# Get a caterpillar at a particular location
mycaterpillar = my_catclass.caterpillar()
 
# Loop until the user clicks the close button.
done = False
# Change to animation mode when user clicks start animation key
start_anim = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while not done:
    if not start_anim:
        for event in pygame.event.get():    # User did something
            if event.type == pygame.QUIT:   # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:     # If user wants to perform an action
                if event.key == pygame.K_SPACE:
                    mycaterpillar.grow()
                if event.key == pygame.K_m:
                    mycaterpillar.move_forward()
                if event.key == pygame.K_d:
                    mycaterpillar.drop_food()
                if event.key == pygame.K_s:
                    start_anim = True
                        
    if start_anim:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True     # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                # If user clicks stop animation key
                if event.key == pygame.K_s:
                    start_anim = False
        mycaterpillar.move_forward()
                
    # Draw the background scene
    draw_background()
    # Draw the caterpillar
    mycaterpillar.draw_caterpillar(screen)
     
    # Limit to 50 frames per second
    clock.tick(50)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit()