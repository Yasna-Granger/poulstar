from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *

t = Tk()
t.geometry('400x400')

def show1():
    messagebox.showinfo(title='Info box', message='operation was succesfull!')
def show2():
    messagebox.showerror(title='Error box', message='operation failed')
def show3():
    messagebox.showwarning(title='Warning box', message='copying this file is dangerous for ur computer, do u still wanna copy it?')
def show4():
    res = messagebox.askquestion(title='Delete file', message='Are u sure u wanna delete this file?')
    if res == 'yes':
        print('file deleted succesfully')
    else:
        print('File still exist')
def show5():
    messagebox.askokcancel(title='This is a message', message='confirmation')
def show6():
    res = messagebox.askyesnocancel(title='Ask yes/no/cancel', message='Wanna close the tab?')
    if res == True:
        print(1)
    elif res == False:
        print(2)
    elif res == None:
        print(3)
def show7():
    messagebox.askretrycancel(title='Ask retry/cancel', message='Do you wanna do this again?')
def show8():
    messagebox.askyesno(title='Ask yes/no', message='Do u wanna exit?')


b1 = Button(t, text='information box', command=show1).grid(row=1, column=1)
b2 = Button(t, text='error box', command=show2).grid(row=1, column=2)
b3 = Button(t, text='warning box', command=show3).grid(row=1, column=3)
b4 = Button(t, text='asking box', command=show4).grid(row=2, column=1)
b5 = Button(t, text='OK/Cancel', command=show5).grid(row=2, column=2)
b6 = Button(t, text='Yes/No/Cancel', command=show6).grid(row=2, column=3)
b7 = Button(t, text='Retry/Cancel', command=show7).grid(row=3, column=1)
b8 = Button(t, text='Yes/No', command=show8).grid(row=3, column=2)


t.mainloop()