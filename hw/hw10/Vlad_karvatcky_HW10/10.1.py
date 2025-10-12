class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides=4)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height
    
rect = Rectangle(5, 3 )
print("Rectangle area:", rect.square())


