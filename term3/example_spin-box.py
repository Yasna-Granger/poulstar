from tkinter import *
import time

t = Tk()
t.geometry('380x300')
t.title('spin box')

spinbox = Spinbox(t, from_=3, to=20, state='readonly')
spinbox.grid(row=1, column=2, columnspan=3, sticky='W')

def show():
    age = int(spinbox.get())
    print(age)
    if continent1.get() == 1:
        print('Iran')
    elif continent1.get() == 2:
        print('Iraq')
    elif continent1.get() == 3:
        print('Turkey')

    if continent2.get() == 1:
        print('Canada')
    elif continent2.get() == 2:
        print('Brazil')
    elif continent2.get() == 3:
        print('Argentina')

    if continent3.get() == 1:
        print('Kenya')
    elif continent3.get() == 2:
        print('Morocco')
    elif continent3.get() == 3:
        print('Nigeria')
    
    if continent4.get() == 1:
        print('Germany')
    elif continent4.get() == 2:
        print('Italy')
    elif continent4.get() == 3:
        print('France')

    #total = int(continent1.get() + continent2.get() + continent3.get() + continent4.get())
    #if total == 4:
    
    #elif total == 5:
        
    #elif total == 6:
        
    #elif total == 7:
        
    #elif total == 8:
        
    #elif total == 9:
        


#Labels
Label(t, text='Age', fg='blue').grid(row=1, column=1)
l1=Label(t, text='Asia', fg='red').grid(row=2, column=1)
l2=Label(t, text='America', fg='red').grid(row=3, column=1)
l3=Label(t, text='Africa', fg='red').grid(row=4, column=1)
l4=Label(t, text='Europe', fg='red').grid(row=5, column=1)
#IntVars
continent1 = IntVar()
continent2 = IntVar()
continent3 = IntVar()
continent4 = IntVar()
#Sets
continent1.set(1)
continent2.set(1)
continent3.set(1)
continent4.set(1)
#Radio Buttons
rb1 = Radiobutton(t, text='Iran', variable=continent1, value = 1)
rb2 = Radiobutton(t, text='Iraq', variable=continent1, value = 2)
rb3 = Radiobutton(t, text='Turkey', variable=continent1, value = 3)

rb4 = Radiobutton(t, text='Canada', variable=continent2, value = 1)
rb5 = Radiobutton(t, text='Brazil', variable=continent2, value = 2)
rb6 = Radiobutton(t, text='Argentina', variable=continent2, value = 3)

rb7 = Radiobutton(t, text='Kenya', variable=continent3, value = 1)
rb8 = Radiobutton(t, text='Morocco', variable=continent3, value = 2)
rb9 = Radiobutton(t, text='Nigeria', variable=continent3, value = 3)

rb10 = Radiobutton(t, text='Germany', variable=continent4, value = 1)
rb11 = Radiobutton(t, text='Italy', variable=continent4, value = 2)
rb12 = Radiobutton(t, text='France', variable=continent4, value = 3)
#Grids
rb1.grid(row=2, column=2)
rb2.grid(row=2, column=3)
rb3.grid(row=2, column=4)

rb4.grid(row=3, column=2)
rb5.grid(row=3, column=3)
rb6.grid(row=3, column=4)

rb7.grid(row=4, column=2)
rb8.grid(row=4, column=3)
rb9.grid(row=4, column=4)

rb10.grid(row=5, column=2)
rb11.grid(row=5, column=3)
rb12.grid(row=5, column=4)

#Check button
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
cb1 = Checkbutton(t, text='Near window', variable = check1)
cb2 = Checkbutton(t, text='First class', variable = check2)
cb3 = Checkbutton(t, text='Additional beverages', variable = check3)
cb1.grid(row=6, column=2)
cb2.grid(row=6, column=3)
cb3.grid(row=6, column=4)

#Button
button = Button(t, text='Show info', command = show).grid(row=7, column=1)

t.mainloop()