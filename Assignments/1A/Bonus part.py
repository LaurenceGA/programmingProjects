import turtle
import random

world = turtle.Screen()

defColours = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "black"]
# Lists are mutable so a duplicate of the information in the defColours list is made with slicing
# cols = copy.copy(defColours)
cols = defColours[:]

def getRandColor(colrs):
    # Colours are removed form the list each time to prevent duplication.
    if len(colrs) == 1:
        colrs = defColours[:]

    col = random.choice(colrs)
    colrs.remove(col)

    return col

def drawRect(t, x1, y1, sizex, sizey):
    # Simply draws a rectangle
    turtle.tracer(0)            # If this is 0, the rectangle is drawn instantly
    drawLine(t, x1 - sizex/2, y1 - sizey/2, x1 + sizex/2, y1 - sizey/2)     # Up
    drawLine(t, x1 - sizex/2, y1 + sizey/2, x1 + sizex/2, y1 + sizey/2)     # Down
    drawLine(t, x1 - sizex/2, y1 - sizey/2, x1 - sizex/2, y1 + sizey/2)     # Left
    drawLine(t, x1 + sizex/2, y1 - sizey/2, x1 + sizex/2, y1 + sizey/2)     # Right
    turtle.update()

def drawLine(turt, x1, y1, x2, y2):
    # draw line from point (x1, y1) to (x2, y2)
    turtle.tracer(0)            # If this line is 0, each line will be drawn instantly
    turt.setheading(turt.towards(x1, y1))
    turt.penup()
    turt.setpos(x1, y1)
    turt.setheading(turt.towards(x2, y2))
    turt.pendown()
    turt.setpos(x2, y2)
    turtle.update()             # Will be called unnecessarily if tracer is set to 1

def getPoints(offx, offy, sizex, sizey, pointNum):
    # This function will return a list of all the points around the rectangle
    pointsl = [[0, 0]] * ((pointNum+1)*4)       # Creates a list of required length
    xsecLength = sizex/(pointNum+1)             # section lengths between each point
    ysecLength = sizey/(pointNum+1)
    pcount = 0                                  # Point number
    for i in range(pointNum+1):
        pointsl[pcount] = [offx - sizex/2 + (xsecLength * i), offy + sizey/2]                       # Up
        pointsl[pcount + (pointNum+1)] = [offx + (sizex/2), offy + sizey/2 - (ysecLength * i)]      # Right
        pointsl[pcount + (pointNum+1) * 2] = [offx + sizex/2 - (xsecLength * i), offy - sizey/2]    # Left
        pointsl[pcount + (pointNum+1) * 3] = [offx - (sizex/2), offy - sizey/2 + (ysecLength * i)]  # Down
        pcount += 1
    return pointsl

def drawPattern(turt, offx, offy, size, points):
    """
    Note: function reduced from sizex and sizey (allowing a rectangle) down to just size to meet the brief.
    """
    # Points is the number of points per side, NOT including the corner points
    # Draw lines between the points around teh box in the given pattern
    sizex = size
    sizey = size
    drawRect(turt, offx, offy, sizex, sizey)        # Basic rectangle to outline the shape

    turtle.tracer(1)                # If this line is 0, the whole pattern will be drawn instantly
    gap = (points + 2)              # Any given point is connected to the point this many points around the rectangle
    pointsl = getPoints(offx, offy, sizex, sizey, points)
    colCount = 0                    # Keep track of when a side has been drawn to know when to change colour
    turt.color(getRandColor(cols))  # Starting colour

    for line in range(len(pointsl)):
        # Makes sure we don't access an index outside of the array, instead looping back to the beginning
        if line+gap > len(pointsl)-1:
            drawLine(turt, pointsl[line][0], pointsl[line][1], pointsl[line+gap - len(pointsl)][0], pointsl[line+gap - len(pointsl)][1])
        else:
            drawLine(turt, pointsl[line][0], pointsl[line][1], pointsl[line+gap][0], pointsl[line+gap][1])

        # Change colour when the time is right
        colCount += 1
        if colCount > (points):
            turt.color(getRandColor(cols))
            colCount = 0

    # Draw a nice looking border around the rectangle
    turt.pensize(10)            # Make it thick
    drawRect(turt, offx, offy, sizex, sizey)
    turt.pensize(1)             # Reset pen size
    turt.penup()
    turt.setpos(offx, offy)     #Sit in the centre of the circle at the end
    turtle.update()


turt = turtle.Turtle()
turt.shape("turtle")
turt.speed(0)          # Speed can be adjusted. Can be made instantaneous if the 1 is turtle.tracer(1) is set to 0 in the function above
turt.pensize(1)

drawPattern(turt, 0, 0, 1200, 25)

world.exitonclick()