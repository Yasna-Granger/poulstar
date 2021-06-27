import threading

def print1to100():
    for i in range(1, 101):
        print(i)
    print('This thread has finished')

t1 = threading.Thread(target=print1to100)
t2 = threading.Thread(target=print1to100)

t1.start() #If we type 't1.join' in the next line, the thread will do the first thread completely, and after that it will start the others
t2.start()