from time import sleep

number = int(input("plz give me a number: "))
counter = 1

while True:
    if counter % number == 0:
        print("HOPE!")
    else:
        print(counter)
    sleep(1)
    counter = counter + 1