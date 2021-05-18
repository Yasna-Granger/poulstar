from tkinter import *
import math
t = Tk()
t.resizable(0, 0)
t.title('Calculator')
t.geometry('290x300')
#Frames
f1=Frame(t, bg='#C5E1A5')
f3=Frame(t, bg='#EC407A')
f4=Frame(t, bg='#EC407A')
#Frame_Placing
f1.place(x=0, y=0, width=300, height=150)
f3.place(x=135, y=150, width=175, height=150)
f4.place(x=0, y=150, width=135, height=150)
#def
def print_number(n):
    result = entry.get()
    length = len(result)
    if n == 'clear':
        entry['state']=NORMAL
        entry.delete(0, length)
        entry['state']='readonly'
    elif n == '0':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '0'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '1':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '1'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '2':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '2'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '3':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '3'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '4':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '4'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '5':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '5'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '6':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '6'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '7':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '7'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '8':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '8'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '9':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '9'
        entry.insert(0, result)
        entry['state']='readonly'


    elif n == 'x':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += 'x'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '÷':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '÷'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '+':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '+'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '-':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '-'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '^':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '^'
        entry.insert(0, result)
        entry['state']='readonly'
    elif n == '%':
        entry['state']=NORMAL
        entry.delete(0, length)
        result += '%'
        entry.insert(0, result)
        entry['state']='readonly'

    if length > 26:
        entry['state'] = NORMAL
        entry.delete(25, length)
        entry['state'] = 'readonly'
#radical
def calculate_sqrt():
    result = int(entry.get())
    my_result.set(str(math.sqrt(result)))
#calculate
def calculate():
    result = ''
    text = str(entry.get())
    counter1 = text.count('+')
    counter2 = text.count('-')
    counter3 = text.count('x')
    counter4 = text.count('÷')
    counter5 = text.count('^')
    counter6 = text.count('%')
    operator = counter1 + counter2 + counter3 + counter4 + counter5 + counter6
    if operator > 1:
        my_result.set(('Too many operators!')) #کد لازم در این قسمت ی بعدا نوشته میشود
    elif operator == 0:
        my_result.set('Enter a operator')
    elif operator == 1:
        if counter1 == 1:
            opperands = text.split('+')
            result = int(opperands[0]) + int(opperands[1])
            my_result.set(result)
        elif counter2 == 1:
            opperands = text.split('-')
            result = int(opperands[0]) - int(opperands[1])
            my_result.set(result)
        elif counter3 == 1:
            opperands = text.split('x')
            result = int(opperands[0]) * int(opperands[1])
            my_result.set(result)
        elif counter4 == 1:
            opperands = text.split('÷')
            result = int(opperands[0]) / int(opperands[1])
            my_result.set(result)
        elif counter5 == 1:
            opperands = text.split('^')
            result = int(opperands[0]) ** int(opperands[1])
            my_result.set(result)
        elif counter6 == 1:
            opperands = text.split('%')
            result = int(opperands[0]) % int(opperands[1])
            my_result.set(result)
            
            
#Buttons
b0 = Button(f4, text='0', height=1 ,width=1, bg='#F48FB1', command=lambda:print_number('0'))
b1 = Button(f4, text='1', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('1'))
b2 = Button(f4, text='2', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('2'))
b3 = Button(f4, text='3', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('3'))
b4 = Button(f4, text='4', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('4'))
b5 = Button(f4, text='5', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('5'))
b6 = Button(f4, text='6', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('6'))
b7 = Button(f4, text='7', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('7'))
b8 = Button(f4, text='8', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('8'))
b9 = Button(f4, text='9', height=2 ,width=5, bg='#F48FB1', command=lambda:print_number('9'))
e9 = Button(f4, text='√', height=1 ,width=5, bg='#00BFA5', command=lambda:calculate_sqrt())
#Button_Placing
b0.grid(row=4, column=1, columnspan=2, sticky='EW')
b1.grid(row=3, column=1)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)
b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)
b7.grid(row=1, column=1)
b8.grid(row=1, column=2)
b9.grid(row=1, column=3)

e9.grid(row=4, column=3)
#Symbol_Buttons
e1 = Button(f3, text='X', height=2 ,width=10, bg='#80DEEA', command=lambda:print_number('x'))
e2 = Button(f3, text='÷', height=2 ,width=10, bg='#CE93D8', command=lambda:print_number('÷'))
e3 = Button(f3, text='+', height=2 ,width=10, bg='#FFCC80', command=lambda:print_number('+'))
e4= Button(f3, text='-', height=2 ,width=10, bg='#A1887F', command=lambda:print_number('-'))
e5 = Button(f3, text='^', height=2 ,width=10, bg='#FF6E40', command=lambda:print_number('^'))
e6 = Button(f3, text='%', height=2 ,width=10, bg='#9FA8DA', command=lambda:print_number('%'))
e7 = Button(f3, text='=', height=1 ,width=10, bg='#6200EA', command=lambda:calculate())
e8 = Button(f3, text='clear', height=1 ,width=10, bg='#CDDC39', command=lambda:print_number('clear'))

#Symbol_Buttons_Placing
e1.grid(row=1, column=1)
e2.grid(row=1, column=2)
e3.grid(row=2, column=1)
e4.grid(row=2, column=2)
e5.grid(row=3, column=1)
e6.grid(row=3, column=2)
e7.grid(row=4, column=1)
e8.grid(row=4, column=2)

#Entry
entry = Entry(t, state='readonly', fg='#8E24AA') #if we type NORMAL instead of 'readonly' we should type with keyboard in the
entry.place(x=60, y=50, width=180, height=50)
#Anwser
my_result =  StringVar()
label_result = Label(f1, textvariable=my_result)
label_result.place(x=90, y=110, width=120, height=25)

mainloop()