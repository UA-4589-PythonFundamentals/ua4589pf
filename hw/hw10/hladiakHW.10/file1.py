class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height])
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


rect = Rectangle(5, 10)
print(rect.area())
