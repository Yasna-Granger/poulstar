import tkinter as tk
import time
import threading

# def thread_count_up():
#     global timer
#     time.sleep(1)
#     timer = timer + 1

def count_up(turn):
    global timer_1, timer_2, stop_counting
    stop_counting = False
    while timer_1 < 100 and timer_2 < 100 and  stop_counting == False:
        time.sleep(0.1)
        if turn == 'orange':
            timer_2 = timer_2 + 1
            time.sleep(0.1)
            timer_green.set(str(timer_2/10))
            window.update()
            print(timer_green.get())
        elif turn == 'green':
            timer_1 = timer_1 + 1
            time.sleep(0.1)
            timer_orange.set(str(timer_1/10))
            window.update()
            print(timer_orange.get())

def start_counting(turn):
    if turn == 'orange':
        # t1 = threading.Thread(target=thread_count_up)
        # t1.start()
        btn_green['state']='disable'
        btn_orange['state']='normal'
        turn = 'green'
        count_up('green')
    elif turn == 'green':
        btn_orange['state']='disable'
        btn_green['state']='normal'
        turn = 'orange'
        count_up('orange')

def reset():
    global timer_1, timer_2, stop_counting
    global turn
    timer_orange.set(0)
    timer_green.set(0)
    btn_orange['state']='normal'
    btn_green['state']='disable'
    turn = 'orange'
    timer_1 = 0
    timer_2 = 0
    stop_counting = True
    
stop_counting = False
timer_1 = 0
timer_2 = 0
turn = 'orange'
window = tk.Tk()
window.geometry('300x200')
window.title('chess match')
btn_orange = tk.Button(window, text='orange', command=lambda: start_counting('green'),
                    bg='orange', activebackground='pink')
btn_green = tk.Button(window, text='green', command=lambda: start_counting('orange'),
                     bg='green', activebackground='pink', state='disable')
btn_reset = tk.Button(window, text='reset', command=reset,
                      bg='black', activebackground='pink', fg='white')
timer_orange = tk.StringVar()
timer_orange.set('0')
timer_green = tk.StringVar()
timer_green.set('0')
label_orange = tk.Label(window, textvariable=timer_orange)
label_green = tk.Label(window, textvariable=timer_green)
btn_orange.grid(row=1, column=3, sticky='NEWS')
btn_green.grid(row=2, column=3, sticky='NEWS')
label_orange.grid(row=1, column=4, sticky='NEWS')
label_green.grid(row=2, column=4, sticky='NEWS')
btn_reset.grid(row=3, column=1, columnspan=2, sticky='NEWS')
tk.mainloop()