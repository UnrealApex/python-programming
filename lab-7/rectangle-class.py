class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height               
        
    def getArea(self):
        """get the area of a rectangle object"""
        return self.width * self.height
    
    def getPerimeter(self):
        """get the perimeter of a rectangle object"""
        return ((2 * self.width) + (2 * self.height))
# initiate two instances of the Rectangle class and give them their attributes
x = Rectangle(4, 40)
y = Rectangle(3.5, 35.7)
print(f'The width of rectangle x is {x.width}')
print(f'The height of rectangle x is {x.height}')
print(f'The area of rectangle x is {x.getArea()}')
print(f'The perimeter of rectangle x is {x.getPerimeter()}')
print("\n")
print(f'The width of rectangle y is {y.width}')
print(f'The height of rectangle y is {y.height}')
print(f'The area of rectangle y is {y.getArea()}')
print(f'The perimeter of rectangle y is {y.getPerimeter()}')
