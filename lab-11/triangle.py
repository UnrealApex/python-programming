import math
import GeometricObject

class Triange(GeometricObject):
    def __init__(self, side1, side2, side3 = 0.0):
        super().__init()
        self.side1 = side1
        self.side2 = side2
        self.side2 = side3

    def getArea(self):
        """return the area of a given Triangle instance"""
        # return 0.5 * (self.base * self.height)
        # get triangle area using Heron's formula
        semi-perimeter = 0.5 * (self.side1 + self.side2 + self.side3)
        return math.sqrt(semi-perimeter * (semi-perimeter - side1) * (semi-perimeter - side2) * (semi-perimeter- side3))

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Triangle side lengths: {self.side1}, {self.side2}, {self.side3}

x = Triangle()

print(isinstance(x, GeometricObject))
