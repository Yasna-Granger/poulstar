from turtle import Turtle, done, textinput
from random import randint
t = Turtle()


def square(x, b):
    y = 1
    while y <= 4:
        t.forward(x)
        t.left(b)
        y += 1


while True:
    x = int(textinput("length", "square's length: "))
    t.penup()
    t.goto(randint(-250,250), randint(-250, 250))
    t.pendown()
    square(x, 90)

