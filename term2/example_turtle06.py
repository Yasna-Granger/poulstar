from turtle import Turtle, done

t = Turtle()


i = 1
while i <= 100:
    x = 1
    while x <= 4:
        t.forward(100)
        t.left(90)
        x = x+1
    i = i+1
    t.left(5)

done()