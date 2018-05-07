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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area.

        Args:
            rect_1 (Rectangle): First Rectangle object to compare.
            rect_2 (Rectangle): Second Rectangle object to compare.

        Returns:
            The biggest rectangle or rect_1 if the area is the same
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new Rectangle with width == height == size.

        Args:
            size (int): the size of the new Rectangle instance.

        Returns:
            The new Rectangle instance.
        """
        cls.number_of_instances += 1
        return Rectangle(size, size)
