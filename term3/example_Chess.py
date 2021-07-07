from tkinter import *
import time

t = Tk()
t.geometry('300x200')
t.title('Chess Math')

turn = 'peach'

def count_up(turn):
    
    if turn == 'peach':
        time.sleep(1)
        Blue_timer.set(float(Blue_timer.get())+0.1)
    elif turn == 'blue':
        time.sleep(1)
        peach_timer.set(float(peach_timer.get())+0.1)

def start_counting(turn):
    if turn == 'peach':
        turn == 'blue'
        count_up('blue')
    elif turn == 'blue':
        turn = 'peach'
        count_up('peach')

def reset():
    peach_timer.set('0')
    Blue_timer.set('0')

#Button
b1 = Button(t, text='Peach', command=start_counting, bg='#F37370')
b2 = Button(t, text='Blue', command=start_counting, bg='#73c2fb')
b3 = Button(t, text='Reset', command=reset, bg='white')

b1.grid(row=1, column=1)
b2.grid(row=1, column=3)
b3.grid(row=3, column=2)

#label
peach_timer = StringVar()
peach_timer.set('0')
Blue_timer = StringVar()
Blue_timer.set('0')

peach_label = Label(t, textvariable=peach_timer)
Blue_label = Label(t, textvariable=Blue_timer)

peach_label.grid(row=2, column=1)
Blue_label.grid(row=2, column=3)

t.mainloop()