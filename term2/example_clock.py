from time import sleep

def clock():
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
                if sec == 59:
                    f = open('term2\\texts\\text05.txt', 'a')
                    f.write(str(min))
                    f.close()

clock()