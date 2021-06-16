from tkinter import *
import tkinter
import tkinter.ttk
from tkinter import messagebox
from tkinter.messagebox import *

t = Tk()
t.resizable(0, 0)
t.title('Form')
t.geometry('470x120')

#def 
def exit_now():
    res = messagebox.askyesno(title='Warning', message='Do u wanna exit?')
    if res == TRUE:
        exit()

def reset():
    res1 = messagebox.askyesno(title='Warning', message='Do u wanna reset?')
    if res1 == TRUE:
        e1.delete(0, len(e1.get()))
        e2.delete(0, len(e2.get()))
        e1.focus()
        combo1.set(' ')
        combo2.set(' ')
        combo3.set(' ')
        gender.set(1)
        spinbox['state'] = NORMAL
        spinbox.delete(0, len(spinbox.get()))
        spinbox.insert(0, 0)
        spinbox['state'] = 'readonly'

def saving():
    res2 = messagebox.askyesno(title='Warning', message='Do u wanna save this information?')
    if res2 == TRUE:
        saves = open('text_form.txt', 'a')
        name = e1.get()
        family = e2.get()
        the_gender = 'Female'
        if gender == 1:
            the_gender = 'Female'
        elif gender == 2:
            the_gender = 'Male'
        elif gender == 3:
            the_gender = 'Prefered not to say'
        the_year = combo1.get()
        the_month = combo2.get()
        the_day = combo3.get()
        the_age = spinbox.get()
        saves.write(name + '\n' + family + '\n' + the_gender + '\n' + the_year + '\n' + the_month + '\n' + the_day + '\n' + the_age + '\n' + '\n')

#label
l1 = Label(t, text='Name:').grid(row=1, column=1)
l2 = Label(t, text='Family:').grid(row=2, column=1)
l3 = Label(t, text='Age:').grid(row=1, column=4)
l4 = Label(t, text='Year:').grid(row=2, column=4)
l5 = Label(t, text='Month:').place(x=251,y=23)
l6 = Label(t, text='Day:').place(x=375,y=23)
l7 = Label(t, text='Gender:').grid(row=3, column=1)

#entry
e1 = tkinter.Entry(t)
e1.grid(row=1, column=2)
e2 = tkinter.Entry(t)
e2.grid(row=2, column=2)

#spinbox
spinbox = Spinbox(t, from_=0, to=120, state='readonly')
spinbox.grid(row=1, column=5, columnspan=5, sticky='W')
#combo box
mylist1 = []
for i in range(1900, 2022):
    mylist1.append(i)
combo1 = tkinter.ttk.Combobox(t, values=mylist1, state='readonly')
combo1.place(x=200,y=23, width=50)

combo2 = tkinter.ttk.Combobox(t, values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agust', 'September', 'October', 'November', 'December'], state='readonly')
combo2.place(x=295,y=23, width=80)

mylist3 = []
for i in range(1, 32):
    mylist3.append(i)
combo3 = tkinter.ttk.Combobox(t, values=mylist3, state='readonly')
combo3.place(x=402,y=23, width=50)

#radio button
gender = IntVar()
rb1 = Radiobutton(t, text='Female', variable=gender, value = 1).place(x=50, y=42)
rb2 = Radiobutton(t, text='Male', variable=gender, value = 2).place(x=120, y=42)
rb3 = Radiobutton(t, text='Prefer not to say', variable=gender, value = 3).place(x=180, y=42)

#Buttons
b1 = Button(t, text='save', command=saving).place(x=345, y=80)
b2 = Button(t, text='Reset', command=reset).place(x=220, y=80)
b3 = Button(t, text='Exit', command=exit_now).place(x=100, y=80)

mainloop()