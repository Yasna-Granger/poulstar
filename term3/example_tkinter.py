import tkinter as tk #ایمپورت کردن کلاس

def show():
    print('hey girl!')
#window
t = tk.Tk()
t.geometry('400x300')#سایز طول و عرض 
t.resizable(0, 0)#هر عددی جز صفر بگزاریم، میتوانیم سول یا عرض را تغییر دهیم و صفحه را بزرگ و کوچک کنیم
t.title('Yangelixx')#انتخاب اسم

#texts
label = tk.Label(t, text='Hello, world!')#باید اول بهش بگوییم در کدام پنجره باز شود و بعد تکس رو بهش بدیم
label.pack()
label2 = tk.Label(t, text='How are you doing?')
label2.pack()#دستور چاپ خط قبل است

#input
e = tk.Entry(t)
e.pack()

#button
b = tk.Button(t, text='Press!', command=show)
b.pack()
#done
t.mainloop()#برای اینکه همیشه باز بمونه