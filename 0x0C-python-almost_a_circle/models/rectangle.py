#!/usr/bin/python3
"""This module contains a rectangle class"""


from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    Inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculates and returns the area value of the rectangle.

        Returns:
            int: The area value.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle using the '#' character,
        accounting for the 'x' and 'y' coordinates.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
                {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""

        if args and len(args) != 0:
            ka = 0
            for arg in args:
                if ka == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif ka == 1:
                    self.width = arg
                elif ka == 2:
                    self.height = arg
                elif ka == 3:
                    self.x = arg
                elif ka == 4:
                    self.y = arg
                ka += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""

        object_dictionary = {'id': self.id, 'width': self.__width,
                             'height': self.__height,
                             'x': self.__x, 'y': self.__y}
        return object_dictionary
