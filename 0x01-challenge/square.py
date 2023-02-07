#!/usr/bin/python3
import math
"""calculate area nad perimeter of a square"""


class square():
    
    width = 0

    
    def __init__(self, *args, **kwargs):
        """initiates square function"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """perimeter of square"""
        return (self.width * 4)

    def __str__(self):
        """return given dimention"""
        return "{}".format(self.width)

if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
