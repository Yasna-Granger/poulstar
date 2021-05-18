from turtle import Turtle, done
from random import randint

t = Turtle()


def glasses():
    t.pensize(5)
    t.color("#deff38")
    t.pencolor("#00b1d9")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(25, 25)
    t.pendown()
    t.forward(30)
    t.left(-90)
    t.begin_fill()
    t.circle(25)
    t.end_fill()



y = 1
while y <= 10:
    t.penup()
    t.goto(randint(-250, 250), randint(-250, 250))
    t.pendown()
    glasses()
    y += 1




done()