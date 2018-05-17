#!/usr/bin/python3
'''
Defines classes BaseGeometry, Rectangle, and Square
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class inherits from Rectangle class.

    '''

    def __init__(self, size):
        '''Initializes a Square.

        Args:
            size (int): Size of the Square.
        '''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
