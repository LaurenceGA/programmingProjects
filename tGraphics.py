import turtle
import math
import random

world = turtle.Screen()     #Create a graphics window

def getRandColor():
    colours = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "black"]

    return random.choice(colours)

def drawSquare(t, size):
    for i in range(4):
        t.forward(size) # move forward with size
        t.right(90) # rotate 90 degree clockwise

def drawTriangle(t, size):
    for i in range(3):
        t.forward(size) # move forward with size
        t.right(120) # rotate 90 degree clockwise

def drawStar(t, size):
    for i in range(5):
        t.forward(size) # move forward with size
        t.right(144) # rotate 90 degree clockwise

def drawCircle(t, r):
    turtle.tracer(0)
    for i in range(360):
        t.forward(2 * math.pi * r / 360)
        t.right(1)
    turtle.update()

def drawSquarePattern(t):
    for i in range(40, 320, 40):
        drawSquare(t, i)

def drawPolygon(t, sideLength, numSides):
    sumOfInteriorAngles = 180 * (numSides - 2)
    ang = 180 - (sumOfInteriorAngles / numSides)
    turtle.tracer(0)
    for i in range(numSides):
        t.forward(sideLength)
        t.right(ang)
    turtle.update()

def drawColSquare():
    n = 32 # number of square
    ang = 360 / n # turning angle
    for i in range(n):
        color = getRandColor()
        john.color(color)
        drawSquare(john, 140)
        john.right(ang)

def drawRandomSquares(t, sw, sh, num):
    for i in range(num):
        color = getRandColor() #get random colour
        rsize = random.randint(40, 200) # generate random size
        rx = random.randint(-sw, sw-rsize) # generate random x pos
        ry = random.randint(-sh+rsize, sh) # generate random y pos
        t.penup() # pen up
        t.setposition(rx, ry) # move to position rx, ry
        t.pendown() # pen down
        t.color(color) # set colour
        #drawSquare(t, rsize) # draw square
        #drawCircle(john, 20)
        drawStar(john, 20)

john = turtle.Turtle()      #Create a turtle named John
john.shape("turtle")        #Give it the shape of a turtle
john.speed(10)
drawRandomSquares(john, 300, 280, 400)
#john.shape("none")

world.exitonclick()     #Wait for the user to click on the canvas