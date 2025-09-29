class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def square(self):
        return self.length * self.width