from time import sleep

counter = 1

while True:
    if counter % 7 == 0:
        print("Hope!")
    else:
        print(counter)
    sleep(1)
    counter = counter + 1