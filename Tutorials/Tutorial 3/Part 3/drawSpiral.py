import turtle
import random

wn = turtle.Screen()

defColours = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "black"]
cols = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "black"]

def getRandColor():
    global cols

    if len(cols) == 1:
        cols += defColours

    col = random.choice(cols)
    cols.remove(col)

    return col

t1 = turtle.Turtle()
t1.speed(0)

def drawSpiral(t, incSize, loopNum):
    size = 0
    for i in range(loopNum):
        t.color(getRandColor())
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        size += incSize


drawSpiral(t1, 10, 100)

wn.exitonclick()