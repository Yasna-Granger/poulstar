from turtle import Turtle, done, Screen

#background
Screen(). bgcolor("gray")

t = Turtle()
t.speed(10000000)

#black_Semicircular
t.color("black")
t.begin_fill()
x = 1
while x <= 181:
    t.forward(2)
    t.left(1)
    x += 1
t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()

#white_Semicircular
y = 1
t.color("white")
t.begin_fill()
while y <= 183:
    t.forward(2)
    t.left(-1)
    y += 1
t.end_fill()

t.penup()
t.goto(0, 114)
t.pendown()

#white_circle
t.begin_fill()
t.circle(57)
t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()

#black_circle
t.color("black")
t.begin_fill()
t.circle(57)
t.end_fill()


t.penup()
t.goto(0, 49)
t.pendown()

#small_white_circle
t.color("white")
t.begin_fill()
t.circle(15)
t.end_fill()

t.penup()
t.goto(0, 163)
t.pendown()

#small_black_circle
t.color("black")
t.begin_fill()
t.circle(15)
t.end_fill()


done()