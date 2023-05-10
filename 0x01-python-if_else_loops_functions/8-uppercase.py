#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            j = 32
        else:
            j = 0
        print("{:c}".format(ord(str[i]) - j), end='')
    print()
