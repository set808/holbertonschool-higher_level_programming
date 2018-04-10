#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in str:
        char = ord(i)
        if 97 <= char <= 122:
            char -= 32
        new += chr(char)
    print('{:s}'.format(new))
