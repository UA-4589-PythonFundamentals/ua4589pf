class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, length, width):
        # Rectangle always has 4 sides
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


#  Get user input
try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Create Rectangle object
    rect = Rectangle(length, width)

    # Display results
    print("\nRectangle details:")
   # print("Number of sides:", rect.sides)
    print("Length:", rect.length)
    print("Width:", rect.width)
    print("Area:", rect.area())

except ValueError:
    print("Please enter valid numeric values for length and width.")

