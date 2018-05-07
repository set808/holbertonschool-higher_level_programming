#!/usr/bin/python3
"""
This module defines a class called Rectangle.
"""


class Rectangle:
    """A class that defines a Rectangle object.

    Attributes:
    number_of_instances (int): The  total number of Rectangle objects.
    print_symbol (str): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Prints the Rectangle object.

        Returns:
            String version of Rectangle object using # symbols
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            return '\n'.join((str(self.print_symbol) * self.width)
                             for row in range(self.height))

    def __repr__(self):
        """Returns a string version of the Rectangle object.

            This representation can be useed to create a new Rectangle object.

        Returns:
            A string that looks like a new Rectangle object
        """
        return ('Rectangle({:d}, {:d})'.format(self.width, self.height))

    def __del__(self):
        """Deletes the Rectangle object and prints a message
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        """Returns the width of the Rectangle object.

        Returns:
            The value of width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle object.

        Args:
            value (int): The value to set width to.
        """
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle object.

        Returns:
            The value of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle object.

        Args:
            value (int): The value to set height to.
        """
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area of the Rectangle.

        Returns:
            The area of the Rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the Rectangle.

        Returns:
        The perimeter of the Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
