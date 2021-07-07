from tkinter import *
import threading
import time

t = Tk()
t.geometry('500x100')
t.title('Drug Alarm')

def count_down(n):
    if n==1:
        timer = int(spin1.get())
        while timer != 0:
            time.sleep(1)
            timer = timer - 1
            drug1.set(timer)
    if n==2:
        timer = int(spin2.get())
        while timer != 0:
            time.sleep(1)
            timer = timer - 1
            drug2.set(timer)
    if n==3:
        timer = int(spin3.get())
        while timer != 0:
            time.sleep(1)
            timer = timer - 1
            drug3.set(timer)
            


def start_counting(n):
    if n == 1:
        timer = spin1.get()
        drug1.set(timer)
    if n == 2:
        timer = spin2.get()
        drug2.set(timer)
    if n == 3:
        timer = spin3.get()
        drug3.set(timer)
    thread1 = threading.Thread(target=count_down, args=(n,))
    thread1.start()
    

#Buttons
b1 = Button(t, text='Asprin', command=lambda: start_counting(1))
b2 = Button(t, text='Metformin', command=lambda: start_counting(2))
b3 = Button(t, text='Dextromethorphan', command=lambda: start_counting(3))

b1.grid(row=3, column=1)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)

#Label
drug1= StringVar()
drug2= StringVar()
drug3= StringVar()

drug1.set('Asprin')
drug2.set('Metformin')
drug3.set('Dextromethorphan')

l1 = Label(t, textvariable=drug1)
l2 = Label(t, textvariable=drug2)
l3 = Label(t, textvariable=drug3)

l1.grid(row=4, column=1)
l2.grid(row=4, column=2)
l3.grid(row=4, column=3)

#Spin boxes

spin1 = Spinbox(t, from_=0, to=60, state='readonly')
spin2 = Spinbox(t, from_=0, to=60, state='readonly')
spin3 = Spinbox(t, from_=0, to=60, state='readonly')

spin1.grid(row=2, column=1)
spin2.grid(row=2, column=2)
spin3.grid(row=2, column=3)

mainloop()