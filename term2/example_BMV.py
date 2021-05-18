from turtle import Turtle, done

t = Turtle()

t.color("blue")
t.begin_fill()
x = 1
while x <= 90:
    t.forward(2)
    t.left(1)
    x += 1
t.end_fill()

done()