from turtle import Turtle, done

t = Turtle()

t.speed(1000000000000000)

length = 1
while True:
    x = 1
    t.color("aqua")
    t.begin_fill()
    while x <= 3:
        t.forward(length)
        t.left(120)
        x += 1
    t.end_fill()
    t.left(10)
    length += 1