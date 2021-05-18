from tkinter import * 
t = Tk()
t.geometry('200x200')
# StringVar / IntVar
x = IntVar() #x = StrVar()
l01 = Label(t, textvariable=x)
a = int(input('Evter the first num: '))
b = int(input('Evter the second num: '))
x.set(a*b)
l01.pack()
t.mainloop()