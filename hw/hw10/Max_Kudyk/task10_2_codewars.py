#TASK 1(Ball-super-ball)

#class Ball:
#    def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type
#--------------------------------------------

#TASK 2()
class Ghost(object):
    counter = 0
    def __init__(self):
        colors=["white","yellow","purple","red"]
        self.color = colors[Ghost.counter % len(colors)]
        Ghost.counter += 1
#--------------------------------------------

#TASK 3()
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]
#--------------------------------------------

#TASK 4()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"

#--------------------------------------------

#TASK 5()
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / ((4 / 3) * math.pi * (self.radius ** 3))
        return round(density, 5)

#--------------------------------------------

#TASK 6()

#--------------------------------------------

