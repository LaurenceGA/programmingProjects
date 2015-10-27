import pygame
import mazeclass

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size = [1000, 500]
screen = pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Maze Project")

# Get a new maze
mazegrid = [[2, 2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2],
            [2, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 2],
            [2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 2],
            [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2],
            [2, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 2],
            [2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 2],
            [2, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
# Another test maze
# mazegrid = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#             [2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2],
#             [2, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 2],
#             [2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2],
#             [2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 2],
#             [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2],
#             [2, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 2],
#             [2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 2],
#             [2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 2],
#             [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2]]

the_maze = mazeclass.Maze(mazegrid)


##########################################################

# Some (silly) sample code for moving one step forward and backward

def forwardbackward(curpos):
    # Warm up at the current position
    moveto(curpos, 3)
    moveto(curpos, 3)
    moveto(curpos, 3)
    moveto(curpos, 3)
    moveto(curpos, 3)
    # Look for positions that can be visited
    neighbourlist = unvisitedneighbours(curpos)    
    if neighbourlist != []:        
        # Select the first position that can be visited
        newpos = neighbourlist[0]      
        # Go to that position
        moveto(newpos, 3)
        # More warm up at the new position
        moveto(newpos, 4)
        moveto(newpos, 4)
        moveto(newpos, 4)
        moveto(newpos, 4)
        moveto(newpos, 4)
        # Move back
        moveto(curpos, 4)


def unvisitedneighbours(curpos):
    # Return list of unvisited positions that can be reached from current position
    x = curpos[0]
    y = curpos[1]
    free = []
    for newpos in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
                if the_maze.grid[newpos[0]][newpos[1]].status == 0:
                    free.append(newpos)     
    return free


def moveto(newpos, status, movebot=True):
    # Mark the new position as being visited
    the_maze.grid[newpos[0]][newpos[1]].status = status
    # If required, move to the new position
    if movebot:
        the_maze.bot_xcoord = newpos[0]
        the_maze.bot_ycoord = newpos[1]
    # Wait a bit and then display the current state of the maze
    pygame.time.delay(30)
    the_maze.display_maze(screen)
    pygame.display.flip()


def movesomesteps(curpos, steps):
    # Move ahead the specified number of steps as long as possible
    # Mark the current position first
    moveto(curpos, 3)
    for step in range(steps):
        neighbour_list = unvisitedneighbours(curpos)

        if not neighbour_list:  # Stop if we don't have any unvisited squares around us
            break

        newpos = neighbour_list[0]  # Just Grab whatever comes first -> order defined by function
        moveto(newpos, 3)
        curpos = newpos


def depthfirsttraversal(curpos):
    # Do a depth-first traversal of all unvisited neighbours
    # Depth first uses a stack as a supporting structure and hence it is most logical to implement recursively
    # Because recursive calls just add to a stack anyway
    moveto(curpos, 3)
    neighbours = unvisitedneighbours(curpos)

    if not neighbours:  # Make sure that we mark branch ends as revisited
        moveto(curpos, 4)

    for neighbour in neighbours:
        # We need to double check that it's unvisited so it doesn't get pushed onto the stack twice by accident
        if the_maze.grid[neighbour[0]][neighbour[1]].status == 0:   # Just makes things go smoother
            depthfirsttraversal(neighbour)      # Push on stack
            moveto(curpos, 4)                   # Walk us back up the stack


def depthfirstsearch(curpos):
    # Perform a depth-first search to find the exit. Once again, recursively
    moveto(curpos, 3)

    # Adapted code from unvisited neighbours to find the exit
    x = curpos[0]
    y = curpos[1]
    for newpos in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= newpos[0] <= the_maze.rows and 0 <= newpos[1] <= the_maze.columns:
                if the_maze.grid[newpos[0]][newpos[1]].status == 5:
                    moveto(newpos, 5)
                    return True     # Return some info to help us know whether to continue

    neighbours = unvisitedneighbours(curpos)
    if not neighbours:  # Make sure branch ends marked as visited
        moveto(curpos, 4)

    for neighbour in neighbours:
        # We need to double check that it's unvisited so it doesn't get pushed onto the stack twice by accident
        if the_maze.grid[neighbour[0]][neighbour[1]].status == 0:
            if depthfirstsearch(neighbour):
                return True     # return all the way up the stack so that we just stop at the exit
            moveto(curpos, 4)


def breadthfirstsearch(curpos):
    # Perform a breadth-first search to find the exit
    # Easier to do this in a while loop rather than recursively as it's supported better by a queue than a stack
    shortest_path = []
    queue = [[curpos]]

    while queue:
        working_node = queue.pop(0)     # De-queue and start working here

        found = False   # So that we can easily jump out of the while loop
        # Once again adapted code from unvisited neighbours
        x = working_node[-1][0]
        y = working_node[-1][1]
        for newpos in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= newpos[0] <= the_maze.rows and 0 <= newpos[1] <= the_maze.columns:
                    if the_maze.grid[newpos[0]][newpos[1]].status == 5:
                        shortest_path = working_node + [newpos]
                        queue = []  # Stops the while loop - don't care about other paths
                        found = True    # Don't do the later stuff

        if not found:
            for neighbour in unvisitedneighbours(working_node[-1]):  # Visit all immediate neighbours
                moveto(neighbour, 3, False)
                queue.append(working_node + [neighbour])    # Adds whole path to queue

    # Actually follow the shortest path here
    for movement in shortest_path:
        moveto(movement, 4)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while not done:
        for event in pygame.event.get():    # User did something
            if event.type == pygame.QUIT:    # If user clicked close
                done = True     # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:     # If user wants to perform an action
                if event.key == pygame.K_f:
                    the_maze.reset(mazegrid)
                    forwardbackward((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_s:
                    the_maze.reset(mazegrid)
                    movesomesteps((the_maze.bot_xcoord, the_maze.bot_ycoord), 15)
                if event.key == pygame.K_t:
                    the_maze.reset(mazegrid)
                    depthfirsttraversal((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_d:
                    the_maze.reset(mazegrid)
                    depthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_b:
                    the_maze.reset(mazegrid)
                    breadthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                         
        the_maze.display_maze(screen)
        # Limit to 50 frames per second
        clock.tick(50)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit()
