#!/usr/bin/python3
def tuple_check(t):
    length = len(t)
    if length == 0:
        new = (0, 0)
        return new
    elif length == 1:
        new = (t[0], 0)
        return new
    return t


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_check(tuple_a)
    tuple_b = tuple_check(tuple_b)
    return tuple(map(sum, zip(tuple_a, tuple_b)))
