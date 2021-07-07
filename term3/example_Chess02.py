import tkinter as tk
import time
import threading

def count_up():
    global timer_1, timer_2, stop_counting, turn, running_threads
    stop_counting = False 
    while timer_1 < 101 and timer_2 < 101 and stop_counting == False:
        time.sleep(0.1)
        if turn == 'red':
            timer_blue.set(str(timer_2/10))
            timer_2 = timer_2 + 1
        elif turn == 'blue':
            timer_red.set(str(timer_1/10))
            timer_1 = timer_1 + 1
    running_threads -= 1
def start_counting():
    global turn, running_threads, tempthread
    if turn == 'red':
        btn_blue['state']='disable'
        btn_red['state']='normal'
        turn = 'blue'
        if running_threads == 0:
            running_threads += 1
            tempthread = threading.Thread(target=count_up)
            tempthread.start()
    elif turn == 'blue':
        btn_red['state']='disable'
        btn_blue['state']='normal'
        turn = 'red'
        if running_threads == 0:
            running_threads += 1
            tempthread = threading.Thread(target=count_up)
            tempthread.start()
def reset():
    global timer_1, timer_2, turn, stop_counting
    timer_red.set('0.0')
    timer_blue.set('0.0')
    btn_red['state']='normal'
    btn_blue['state']='disable'
    turn = 'blue'
    timer_1 = 0
    timer_2 = 0
    stop_counting = True

running_threads = 0
stop_counting = False
timer_1 = 0
timer_2 = 0
turn = 'blue'
window = tk.Tk()
window.geometry('300x200')
window.title('chess match')
btn_red = tk.Button(window, text='red', command=start_counting,
                    bg='red', activebackground='pink')
btn_blue = tk.Button(window, text='blue', command=start_counting,
                     bg='blue', activebackground='pink', state='disable')
btn_reset = tk.Button(window, text='reset', command=reset,
                      bg='black', activebackground='pink', fg='white')
timer_red = tk.StringVar()
timer_red.set('0.0')
timer_blue = tk.StringVar()
timer_blue.set('0.0')
label_red = tk.Label(window, textvariable=timer_red)
label_blue = tk.Label(window, textvariable=timer_blue)
btn_red.grid(row=1, column=1, sticky='NEWS')
btn_blue.grid(row=2, column=1, sticky='NEWS')
label_red.grid(row=1, column=2, sticky='NEWS')
label_blue.grid(row=2, column=2, sticky='NEWS')
btn_reset.grid(row=3, column=1, columnspan=2, sticky='NEWS')
tk.mainloop()