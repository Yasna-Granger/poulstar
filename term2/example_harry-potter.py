from turtle import Turtle, Screen, done, textinput

t = Turtle()
s = Screen()

t.speed(1000000000000000000000000000000)
t.shape("circle")
s.bgpic("term2/Images/hugwarts.gif")
s.setup(width = 400, height = 330)
t.color("#fffb85")
t.begin_fill()
t.circle(20)
t.end_fill()
t.left(270)
t.color("red")
t.forward(50)
t.penup()
t.goto(0,-25)
t.pendown()
t.left(45)
t.forward(20)
t.stamp()
t.penup()
t.goto(0, -25)
t.pendown()
t.left(270)
t.forward(20)
t.stamp()
t.penup()
t.goto(0 , -50)
t.pendown()
t.left(90)
t.forward(35)
t.stamp()
t.penup()
t.goto(0 , -50)
t.pendown()
t.left(-90)
t.forward(35)
t.stamp






done()