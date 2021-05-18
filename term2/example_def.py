from turtle import Turtle, done
from random import randint

t = Turtle()
t.color("black")
def square():
    t.penup()
    t.goto(randint(-250 , 250), randint(-250 , 250))
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

x  = 1
while x <= 100:
    square()

done()