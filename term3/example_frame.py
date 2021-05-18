from tkinter import *

t = Tk()
t.geometry('400x400')
f1=Frame(t, bg='pink')
f2=Frame(t, bg='blue')
f3=Frame(t, bg='yellow')
f4=Frame(t, bg='lime')

f1.place(x=0, y=0, width=200, height=200)
f2.place(x=200, y=0, width=200, height=200)
f3.place(x=200, y=200, width=200, height=200)
f4.place(x=0, y=200, width=200, height=200)

l1=Label(f4, text='Yasna', padx=100, bg='lime', fg='green')
l1.pack(side='left')

t.mainloop()