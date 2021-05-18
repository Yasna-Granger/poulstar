from time import sleep

x = 0
f = open('term2/texts/text04', 'a')
while x <= 100:
    sleep(1)
    mod = x % 2
    if mod == 1:
        f.write(str(x) + '\n')
    x += 1