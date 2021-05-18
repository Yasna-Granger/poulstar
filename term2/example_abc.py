from turtle import Turtle
from random import randint

t = Turtle()
t.speed(10000000000000000000)

def square(r):
    a = 1
    while a <= 4:
        t.forward(r)
        t.left(90)
        a += 1

while True:
    t.penup()
    file = open('C:\\Users\\G.V Shop\\PycharmProjects\\Luna_Lovegood\\term2\\text02.txt', 'a')
    x = randint(-500, 500)
    y = randint(-500, 500)
    r = randint(5, 100)

    file.write("(" + "x: " + str(x) + ", y: " + str(y) + ", r: " + str(r) + ")" + '\n')
    file.close()

    t.goto(x, y)
    t.pendown()
    square(r)
