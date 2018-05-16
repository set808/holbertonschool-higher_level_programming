#!/usr/bin/python3
'''
Defines a function to check to see if objects are instance of a class
'''


def is_kind_of_class(obj, a_class):
    '''Checks if object is instance of a class.

    Args:
        obj: object to check.
        a_class: class to check against.

    Return:
    Returns True if it is an instance, False otherwise.
    '''
    return isinstance(obj, a_class)
