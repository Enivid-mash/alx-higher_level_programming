#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv) - 1))
    i = 0
    for arg in argv[1:]:
        print("{}: {}".format(i+1, arg))
        i += 1
