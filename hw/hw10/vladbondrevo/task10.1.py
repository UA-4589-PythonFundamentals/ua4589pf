class Polygon():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
class Rectangle(Polygon):
    def square(self):
        return self.length * self.width


a = Rectangle(8, 6)
print(a.square())
