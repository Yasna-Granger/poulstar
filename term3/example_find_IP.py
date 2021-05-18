import os
from os.path import *

home = expanduser('~')

dl_path = home + '\\Downloads'

def main():
    if not os.path.exist(dl_path):
        print("path does'nt exist")
        os.makedirs(dl_path)

if __name__ == '__main__':
    a = 1
    while a<= 50:
        main()
        a += 1