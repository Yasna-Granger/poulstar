import turtle
import threading

def move_fd(t: turtle.Pen, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fd(500)

t1 = turtle.Pen()
move_fd(t1, -200, 200)
t2 = turtle.Pen()
move_fd(t2, -200, 100)
t3 = turtle.Pen()
move_fd(t3, -200, 0)
t4 = turtle.Pen()
move_fd(t4, -200, -100)
t5 = turtle.Pen()
move_fd(t5, -200, -200)

turtle.done()