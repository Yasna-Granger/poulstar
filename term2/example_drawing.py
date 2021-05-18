from turtle import Turtle, done, shapesize
t = Turtle()
t.speed(100000)
t.penup()
t.goto(0, -50)
t.pendown()

a = 1
while a <= 10:
    t.forward(10)
    t.left(9)
    a = a + 1

t.forward(90)

b = 1
while b <= 20:
    t.forward(10)
    t.left(9)
    b = b + 1

t.forward(90)

c = 1
while c <= 10:
    t.forward(10)
    t.left(9)
    c = c + 1

t.penup()
t.goto(70, 50)
t.pendown()


d = 1
while d <= 5:
    t.forward(2)
    t.left(15)
    d = d +1

t.left(20)
t.forward(10)

t.forward(10)

d = 1
while d <= 5:
    t.forward(2)
    t.left(15)
    d = d +1

t.penup()
t.goto(-60, 50)
t.pendown()

d = 1
while d <= 5:
    t.forward(2)
    t.left(15)
    d = d +1

t.left(20)
t.forward(10)

t.forward(10)

d = 1
while d <= 5:
    t.forward(2)
    t.left(15)
    d = d +1






done()