import math
from geometric_object import GeometricObject

class Triangle(GeometricObject):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getArea(self):
        """return the area of a given Triangle instance"""
        # return 0.5 * (self.base * self.height)
        # get triangle area using Heron's formula
        semi_perimeter = 0.5 * (self.side1 + self.side2 + self.side3)
        return math.sqrt(semi_perimeter * (semi_perimeter - self.side1) * (semi_perimeter - self.side2) * (semi_perimeter - self.side3))

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Triangle side lengths: {self.side1}, {self.side2}, {self.side3}"

x = Triangle(1, 2, 3)

print(isinstance(x, GeometricObject))
x.setColor("blue")
x.setFilled(True)
print(x.getColor())
print(x.isFilled())
