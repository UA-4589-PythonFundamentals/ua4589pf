class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, a, b):
        super().__init__([a,b,a,b])
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

rect = Rectangle(5,4)

print(f"Area of rectangle:{rect.area()}")
