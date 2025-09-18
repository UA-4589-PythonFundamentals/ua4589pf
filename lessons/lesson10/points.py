# class Point:
#     def __init__(self, x=0, y=0):
#         print(f"Calling Point.__init__ with x={x}, y={y}")
#         self.x = x
#         self.y = y

#     def __del__(self):
#         print(f"Calling Point.__del__ for Point_x({self.x}, {self.y})")

#     def move(point, dx, dy):
#         point.x += dx
#         point.y += dy

#     def distance(point1, point2):
#         print(f"Calling Point.distance with {point1}, {point2}")
#         return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

#     def __str__(self):
#         print("Calling Point.__str__")
#         return f"Point({self.x}, {self.y})"

# def foo():
#     p = Point(3, 4)
#     print(p)
#     print("Exiting foo()")
# print("Creating point p in foo()")
# foo()
# print("main Exited foo()")
# p1 = Point(1, 2)
# p2 = Point(4, 6)
# print(p1)
# print(p2)
# print("Distance:", Point.distance(p1, p2))
# print("distance:", p1.distance(p2))  # This will raise an error
# Point.move(p1, 2, 3)
# print(p1)
# s = str(p1)
# print(s)

import re


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        # return (self.x, self.y) < (other.x, other.y)
        return self.distance(Point(0, 0)) < other.distance(Point(0, 0))
    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)
    
# p1 = Point(1, 2)
# p2 = Point(4, 6)
# print(p1)
# print(p2)
# print("Distance:", p1.distance(p2))
# p3 = p1 + p2
# print(p3)

# points = [Point(7, 8), Point(1, 2), Point(5, 6), Point(3, 4)]
# print(points)
# points.sort()
# print(points)

class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y)
        self.color = color

    def __str__(self):
        return f"ColorPoint({self.x}, {self.y}, {self.color})"
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    
cp = ColorPoint(1, 2, "red")
print(cp)
color_points = [ColorPoint(7, 8, "red"), ColorPoint(1, 2, "blue"), ColorPoint(5, 6, "green"), ColorPoint(3, 4, "yellow")]
print(color_points)
color_points.sort()
print(color_points)
print(cp.__hash__())