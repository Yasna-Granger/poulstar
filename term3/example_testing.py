from tkinter import *
import tkinter
import tkinter.ttk
from tkinter import messagebox
from tkinter.messagebox import *

t = Tk()
t.resizable(0, 0)
t.title('Your info')
t.geometry('250x100')

l1 = Label(t, text='Name:').grid(row=1, column=1)
l2 = Label(t, text='Family:').grid(row=2, column=1)
l3 = Label(t, text='Phone number:').grid(row=3, column=1)

def saving():
    res2 = messagebox.askyesno(title='Warning', message='Do u wanna save this information?')
    if res2 == TRUE:
        name = e1.get()
        family = e2.get()
        phone = e3.get()
        file_name = name + ' ' + family
        the_file = file_name + '.txt'
        saves = open(the_file , 'a')
        saves.write(name + '\n' + family + '\n' + phone)
        

e1 = tkinter.Entry(t)
e1.grid(row=1, column=2)
e2 = tkinter.Entry(t)
e2.grid(row=2, column=2)
e3 = tkinter.Entry(t)
e3.grid(row=3, column=2)

b1 = Button(t, text='save', command=saving).grid(row=5, column=2)

t.mainloop()