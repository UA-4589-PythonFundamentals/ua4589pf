class Polygon:
    def __init__(self, sides_count):
        self.sides_count = sides_count
    
class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.height = height
        self.width = width

    def area (self):
        return self.width * self.height
    