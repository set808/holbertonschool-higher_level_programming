#!/usr/bin/python3
for i in range(97, 123):
    if i == ord('e') or i == ord('q'):
        continue
    else:
        print('{:s}'.format(chr(i)), end='')
