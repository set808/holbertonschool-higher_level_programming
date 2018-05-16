#!/usr/bin/python3
'''
Defines classes BaseGeometry, Rectangle, and Square
'''


class BaseGeometry:
    '''BaseGeometry class

    '''

    def area(self):
        '''defines area function

        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates value

        Args:
            name (str): the name of something
            value (int): some value that wasn't explained
        '''

        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    ''' Rectangle class inherits from BaseGeometry

    '''

    def __init__(self, width, height):
        """Initializes a Rectangle object.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return '[{:s}] {:d}/{:d}'.format(type(self).__name__,
                                         self.__width, self.__height)

    def area(self):
        '''defines area function.

        '''
        return self.__height * self.__width


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
