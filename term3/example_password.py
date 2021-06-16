from tkinter import *
import tkinter
import tkinter.ttk
from tkinter import messagebox
from tkinter.messagebox import *

t = Tk()
t.resizable(0, 0)
t.title(':)')
t.geometry('250x125')
def check():
    user = e1.get()
    password = e2.get()
    if user == 'Yasna':
        if password == '2581825499':
            messagebox.showinfo(title=':)', message='Logging in was succesfull!')
        else:
            res = messagebox.askyesno(title=':(', message='Sth is wrong, Do u wanna try again?')
            if res == FALSE:
                exit()
    if user == 'Setia':
        if password == '2672936499':
            messagebox.showinfo(title=':)', message='Logging in was succesfull!')
        else:
            res = messagebox.askyesno(title=':(', message='Sth is wrong, Do u wanna try again?')
            if res == FALSE:
                exit()


l1 = Label(t, text='Username:').grid(row=1, column=1, padx=10, pady=10)
l2 = Label(t, text='Password:').grid(row=2, column=1)

e1 = tkinter.Entry(t)
e1.grid(row=1, column=2)
e2 = tkinter.Entry(t)
e2.grid(row=2, column=2)

b1 = Button(t, text='Done', command=check).place(x=125, y=80)

t.mainloop()