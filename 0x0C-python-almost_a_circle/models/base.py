#!/usr/bin/python3
'''
Defines a class Base
'''


class Base:
    '''Base of all other classes in this project

    goal is to manage id attribute in all future classes

    Attributes:
        __nb_objects (int): number of Base objects created
        id (int): the id of the object
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
