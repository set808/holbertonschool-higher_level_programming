#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for i, char in enumerate(my_list):
        if (char == 'c' or char ==  'C'):
            del my_list[i]
    return ''.join(my_list)
