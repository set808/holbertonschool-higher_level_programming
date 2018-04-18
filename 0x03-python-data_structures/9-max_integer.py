#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for i, num in enumerate(my_list[1:]):
            if num > max_int:
                max_int = num
        return max_int
    else:
        return None
