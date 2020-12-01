from typing import Counter


first_num = int(input("plz gime me the first number: "))
second_num = int(input("plz gime me the second number: "))
space = int(input("give me the spaces between numbers?: "))

for i in range(first_num, second_num, space):
    print(i)