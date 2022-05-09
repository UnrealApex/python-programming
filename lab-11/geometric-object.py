import math
class GeometricObject:
    def __init__(self):

        class Triange(GeometricObject):
            # def __init__(self, side1, side2, side3 = 0.0, base = "side1", height = 0.0)
            def __init__(self, side1, side2, side3 = 0.0)
                self.side1 = side1
                self.side2 = side2
                self.side2 = side3

            def getArea(self):
                """return the area of a given Triangle instance"""
                # return 0.5 * (self.base * self.height)
                semi-perimeter = 0.5 * (self.side1 + self.side2 + self.side3)
                return math.sqrt(semi-perimeter * (semi-perimeter - side1) * (semi-perimeter - side2) * (semi-perimeter- side3))

