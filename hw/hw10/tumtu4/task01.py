class Poligon:
    def __init__(self, lst_of_sides: list):
        self.sides = lst_of_sides

    def square(self):
        pass


class Rectangle(Poligon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.angle = 90
    
    def square(self):
        return self.length * self.width
    

r = Rectangle(10, 5)
print("Square of Rectangle -", r.square())

