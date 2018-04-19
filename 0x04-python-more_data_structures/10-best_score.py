#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sort = sorted(a_dictionary, key=a_dictionary.get, reverse=True)
        return sort[0]
    else:
        return None
