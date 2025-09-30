class Polygon:
    
    def __init__(self, sides):
        self.sides = sides
    

class Rectangle(Polygon):
    
    def __init__(self, length, width):
        super().__init__(4) 
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    
rect = Rectangle(5, 3)
print(f"Area: {rect.calculate_area()}")