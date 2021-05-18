from turtle import Turtle, done
from random import randint

t = Turtle()
t.speed(1000000000000)

def square():
    random = randint(10, 50)
    t.pencolor('black')
    a = 1
    while a <= 4:
        t.forward(random)
        t.left(90)
        a += 1
    
    
    
while True:
    x = randint(-500, 500)
    y = randint(-500, 500)
    file = open("C:\\Users\\G.V Shop\\PycharmProjects\\Luna_Lovegood\\term2\\texts\\text02.txt", 'a')
    file.write('(' + 'x: ' + str(x) + ' ' + 'y: ' + str(y) + ')' + "\n")
    file.close()
    t.penup()
    t.goto(x, y)
    t.pendown()
    square()