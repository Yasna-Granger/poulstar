from tkinter import * 
import tkinter
def hahaha():
    print('test')

root = tkinter.Tk()
root.resizable(0, 0)
root.geometry('300x300')
btn1 = Button(root, text='button1', bg = 'red', command = hahaha).pack(side = TOP, expand=1, fill='both')#expand=>0/1 #fill=>both/none/x/y
btn2 = Button(root, text='button2', bg = 'black', fg='white', command = hahaha).pack(side = BOTTOM)
btn3 = Button(root, text='button3', bg = 'pink', command = hahaha).pack(side = LEFT)
btn4 = Button(root, text='button4', bg = 'yellow', command = hahaha).pack(side = RIGHT)
mainloop()