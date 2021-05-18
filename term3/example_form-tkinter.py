import tkinter
t = tkinter.Tk()
def show():
    name = e01.get()
    family = e02.get()
    age = e03.get()
    print(name, family, age)
t.title('form')
#name
label01 = tkinter.Label(t, text='What is your name?', background='#CE93D8', foreground='#4A148C')
label01.grid(row=1, column=1)
e01 = tkinter.Entry(t, bg='#B2EBF2')
e01.grid(row=1, column=2)
#family
label02 = tkinter.Label(t, text='What is your family name?', bg='#80DEEA', fg='#006064')#به جای background میشه از bg هم استفاده کرد
label02.grid(row=2 ,column=1)
e02 = tkinter.Entry(t, bg='#B2EBF2')
e02.grid(row=2 ,column=2)
#age
label03 = tkinter.Label(t, text='What is your age?', bg='#FFF59D', fg='#F57F17')
label03.grid(row=3 ,column=1)
e03 = tkinter.Entry(t, bg='#B2EBF2')
e03.grid(row=3 ,column=2)
#done-button
b = tkinter.Button(t, text='press if you are done!', command=show, bg='#ff8a80', fg='#E91E63')
b.grid(row=4, column=1, columnspan=2)#اگر دستور  sticky='EW' را هم بنویسیم به هردو سمت میچسبد

t.mainloop()