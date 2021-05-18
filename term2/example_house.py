from turtle import Turtle, done, Screen
from random import randint

#variables
t = Turtle()
s = Screen()
x = 1
y = 1
z = 1
m = 1

t.speed(100000)
s.setup(width=500, height=500)

#grass
t.penup()
t.goto(-250, 0)
t.pendown()
t.color("#046e00")
t.begin_fill()
t.forward(500)
t.left(-90)
t.forward(250)
t.left(-90)
t.forward(500)
t.left(-90)
t.forward(250)
t.left(-90)
t.end_fill()

#sky
t.color("#73ffea")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(250)
t.left(90)
t.forward(500)
t.left(90)
t.forward(250)
t.left(90)
t.end_fill()


#woods

#location
t.penup()
t.goto(-250, -125)
t.pendown()

#color
t.color("#633700")
t.pencolor("black")

t.begin_fill()
while x <= 15:
    t.left(45)
    t.forward(25)
    t.left(-90)
    t.forward(25)
    t.left(-45)
    t.forward(125)
    t.left(-90)
    t.forward(36)
    t.left(-90)
    t.forward(125)
    t.left(-90)
    t.forward(35)
    x += 1
t.end_fill()

while m <= 15:
    t.penup()
    t.goto(randint(-250, 250), randint(-110, 0))
    t.pendown()

    t.color(randint("#ff008c, #ff61b8"))
    t.begin_fill()
    while z <= 4:
        t.circle(10)
        t.left(90)
        z += 1
    t.end_fill()
    m += 1




done()