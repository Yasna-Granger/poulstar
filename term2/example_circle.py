from turtle import Turtle, done

t = Turtle()


t.color("orchid")
t.begin_fill()
x = 1
while x <= 72:
    t.forward(5)
    t.left(5)
    x += 1
t.end_fill()

done()