import tkinter
t = tkinter.Tk()
t.geometry('300x180')
t.resizable(0, 0)
def show():
    name = e01.get()
    family = e02.get()
    age = e03.get()
    print(name, family, age)
t.title('form')
#name
label01 = tkinter.Label(t, text='What is your name?', background='#CE93D8', foreground='#4A148C')
label01.place(x=5, y=10,  width=105, height=20)
e01 = tkinter.Entry(t, bg='#B2EBF2')
e01.place(x=150, y=10,  width=150, height=20)
#family
label02 = tkinter.Label(t, text='What is your family name?', bg='#80DEEA', fg='#006064')
label02.place(x=5, y=40,  width=140, height=20)
e02 = tkinter.Entry(t, bg='#B2EBF2')
e02.place(x=150, y=40,  width=150, height=20)
#age
label03 = tkinter.Label(t, text='What is your age?', bg='#FFF59D', fg='#F57F17')
label03.place(x=5, y=70,  width=100, height=20)
e03 = tkinter.Entry(t, bg='#B2EBF2')
e03.place(x=150, y=70,  width=150, height=20)
#done-button
b = tkinter.Button(t, text='press if you are done!', command=show, bg='#ff8a80', fg='#E91E63')
b.place(x=80, y=120,  width=120, height=50)

t.mainloop()