from time import sleep
from threading import Thread


def clock(a):
    sec = 0
    min = 0
    hour = 0
    while True:
        sleep(1)
        sec += 1
        print(hour, ":", min, "\'", ":", sec,  "\"" )
        if sec >= 60:
            sec = 0
            min += 1
            if min >= 60:
                min = 0
                hour += 1

#thread=کلا برای این استفاده میشه که اگه بخوایم از یک تابع چندبار بنویسیم
t1 = Thread(target=clock, args=(0,)) #args همان argument
t2 = Thread(target=clock, args=(0,))#args به تابع مقدارمیده

t1.start()
t2.start()