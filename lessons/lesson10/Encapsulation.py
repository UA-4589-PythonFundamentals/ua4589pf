class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self._y = y
        self.__z = z
    
    def __str__(self):
        return f"Point({self.x}, {self._y}, {self.__z})"

    def get_y(self):
        print("Getter for y called")
        return self._y
    def set_y(self, value):
        print("Setter for y called")
        if value < 0:
            self._y = 0
        else:
            self._y = value
    y = property(get_y, set_y)

    @property
    def z(self):
        print("Getter for z called")
        return self.__z
    @z.setter
    def z(self, value):
        print("Setter for z called")
        if value < 0:
            self.__z = 0
        else:
            self.__z = value

    def print_info(self):
        print(self.x, self._y, self.__z)
    def print_info(self, prefix):
        print(prefix, self.x, self._y, self.__z)

# p = Point(1, 2, 3)
# print(p)
# print(p.x)
# print(p._y)
# print(p._Point__z)  # name mangling
# p._Point__z = 10
# print(p)
# p.set_y(20)
# print(p.get_y())
# p.set_y(-20)
# print(p.get_y())
# p.y = 30
# print(p.y)
# p.z = 40
# print(p.z)
# print(p)
# p.print_info("Custom prefix:")
# # p.print_info()
p = Point(1, 2, 3)
print(p.__dict__)
for key, value in Point.__dict__.items():
    print(f"{key:<25} : {value}")