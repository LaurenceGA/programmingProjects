import turtle
import random
import math

world = turtle.Screen()

defColours = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "black"]
cols = defColours[:]

def getRandColor(cols):
    # Colours are removed form the list each time to prevent duplication.
    if len(cols) == 1:
        cols = defColours[:]

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
    turtle.tracer(1)            # If this line is 0, each line will be drawn instantly
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

def drawPattern(turt, offx, offy, radiusOut, stepOut, radiusIn, stepIn):
    outerPoints = drawCricle(turt, offx, offy, radiusOut, stepOut)
    innerPoints = drawCricle(turt, offx, offy, radiusIn, stepIn)

    turtle.tracer(1)
    outerPNum = 0
    innerPNum = 0

    while True:
        if outerPNum >= len(outerPoints):
            outerPNum = 0
        if innerPNum >= len(innerPoints):
            innerPNum = 0

        drawLine(turt, outerPoints[outerPNum][0], outerPoints[outerPNum][1], innerPoints[innerPNum][0], innerPoints[innerPNum][1])

        outerPNum += 1
        innerPNum += 1

    turt.penup()
    turt.setpos(offx, offy)     #Sit in the centre of the circle at the end
    turtle.update()


turt = turtle.Turtle()
turt.shape("turtle")
turt.speed(0)          # Speed can be adjusted. Can be made instantaneous if the 1 is turtle.tracer(1) is set to 0 in the function above

drawPattern(turt, 0, 0, 500, 52, 300, 32)

world.exitonclick()
