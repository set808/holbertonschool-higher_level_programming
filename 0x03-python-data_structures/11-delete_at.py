#!/usr/bin/python3
def delete_at(mylist=[], idx=0):
    if idx < 0 or idx > len(mylist) - 1:
        return mylist
    del mylist[idx]
    return mylist
