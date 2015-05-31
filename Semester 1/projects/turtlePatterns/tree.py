import turtle
import random

wn = turtle.Screen()

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.penup()
t.sety(-wn.window_height()/2+50)

maxBranch = 4

class node:
    def __init__(self, t, x, y, head, width, length, dist, subnodes):
        self.turt = t
        self.x = x
        self.y = y
        self.head = head
        self.width = width
        self.length = length

        self.distfromstart = dist

        self.drawNode()

        self.nodelist = []
        for i in range(subnodes):
            if self.width > 3:
                newHead = random.randint(round(-30), round(30))
                self.nodelist.append(node(t, self.tip[0], self.tip[1], self.head + newHead, self.width*0.7, self.length*0.7, self.distfromstart+1, random.randint(1, maxBranch)))
            else:
                self.drawleaf()
                # self.turt.setheading(self.head)

            self.turt.setheading(self.head + 90)

    def drawNode(self):
        self.turt.color("#66512D")
        self.turt.pensize(self.width)
        self.turt.penup()
        self.turt.goto(self.x, self.y)
        self.turt.right(self.head)
        self.turt.pendown()
        self.turt.forward(self.length)
        self.tip = [self.turt.xcor(), self.turt.ycor()]

    def drawleaf(self):
        turtle.tracer(0)
        self.turt.color("green")
        self.turt.pensize(random.randint(5, 10))
        self.turt.penup()
        self.turt.right(random.randint(-20, 20))
        self.turt.pendown()
        self.turt.forward(10)
        # turtle.tracer(1)

turtle.tracer(0)
branchLength = 300
branchWidth = 40
curPos = [t.xcor(), t.ycor()]
positions = [curPos]
branchNum = 1

t.setheading(90)


base = node(t, curPos[0], curPos[1], 0, branchWidth, branchLength, 1, 4)
turtle.update()

wn.exitonclick()
