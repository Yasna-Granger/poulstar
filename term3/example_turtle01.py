import turtle
import threading

def move_fd(t: turtle.Pen, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fd(500)

t1 = turtle.Pen()
#move_fd(t1, -200, 200)
t2 = turtle.Pen()
#move_fd(t2, -200, 100)
t3 = turtle.Pen()
#move_fd(t3, -200, 0)
t4 = turtle.Pen()
#move_fd(t4, -200, -100)
t5 = turtle.Pen()
#move_fd(t5, -200, -200)

#threads are based on your CPU strenght

th1 = threading.Thread(target=move_fd, args=(t1, -200, 200))
th2 = threading.Thread(target=move_fd, args=(t2, -200, 100))
th3 = threading.Thread(target=move_fd, args=(t3, -200, 0))
th4 = threading.Thread(target=move_fd, args=(t4, -200, -100))
th5 = threading.Thread(target=move_fd, args=(t5, -200, -200))

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()

turtle.done()