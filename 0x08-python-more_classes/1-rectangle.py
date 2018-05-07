#!/usr/bin/python3
"""
This module defines a class called Rectangle.
"""

class Rectangle:
    """A class that defines a Rectangle object.
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

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

