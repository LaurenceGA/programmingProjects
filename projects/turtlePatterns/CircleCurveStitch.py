import turtle
import random
import copy
import math

world = turtle.Screen()

defColours = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "black"]
# Lists are mutable so the copy module is used to create a duplicate of the information in the defColours list instead of a reference to it
cols = copy.copy(defColours)

def getRandColor(cols):
    # Colours are removed form the list each time to prevent duplication.
    if len(cols) == 1:
        cols = copy.copy(defColours)

    col = random.choice(cols)
    cols.remove(col)

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


def drawCricle(t, x1, y1, r, step):
    turtle.tracer(0)
    pointsl = []
    t.penup()
    circumfrence = 2*math.pi*r
    t.setpos(x1 - (circumfrence/step)/2, y1 + r)
    t.pendown()
    t.setheading(0)
    for i in range(step):
        pointsl.append([t.xcor(), t.ycor()])
        t.forward(circumfrence/step)
        t.right(360/step)
    t.penup()
    t.setpos(x1, y1)
    turtle.tracer(1)

    return pointsl

def drawPattern(turt, offx, offy, radius, step):
    # Points is the number of points per side, NOT including the corner points
    # Draw lines between the points around teh box in the given pattern
    # drawRect(turt, offx, offy, sizex, sizey)        # Basic rectangle to outline the shape
    pointsl = drawCricle(turt, offx, offy, radius, step)

    turtle.tracer(1)
    for p in range(len(pointsl)):
        turt.color(getRandColor(cols))
        for p2 in range(len(pointsl)-3):
            if not p+p2+2 > len(pointsl)-1:
                drawLine(turt, pointsl[p][0], pointsl[p][1], pointsl[p+p2+2][0], pointsl[p+p2+2][1])
            else:
                drawLine(turt, pointsl[p][0], pointsl[p][1], pointsl[p+p2+2 - len(pointsl)][0], pointsl[p+p2+2 - len(pointsl)][1])



    turtle.update()
    # Draw a nice looking border around the rectangle
    # turt.pensize(10)            # Make it thick
    # drawRect(turt, offx, offy, sizex, sizey)
    # turt.pensize(1)             # Reset pen size
    turt.penup()
    turt.setpos(offx, offy)     #Sit in the centre of the circle at the end
    turtle.update()


turt = turtle.Turtle()
turt.shape("turtle")
turt.speed(0)          # Speed can be adjusted. Can be made instantaneous if the 1 is turtle.tracer(1) is set to 0 in the function above

drawPattern(turt, 0, 0, 500, 32)

world.exitonclick()
