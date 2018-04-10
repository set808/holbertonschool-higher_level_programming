#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in str:
        char = ord(i)
        if ord('a') <= char <= ord('z'):
            char -= 32
        new += chr(char)
    print('{:s}'.format(new))
