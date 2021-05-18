from turtle import Turtle, penup
from random import randint

t = Turtle()
t.speed(10000000)

while True:
    t.penup()
    t.goto(randint(-250, 250), randint(-250, 250))
    t.pendown()

    t.color("#" + str(randint(100000, 999999)))
    t.begin_fill()
    t.circle(randint(20,90))
    t.end_fill()
