#I. Ball-super-ball
class Ball:
    def __init__(self, type='regular'):
        self.ball_type = type

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)
print(ball2.ball_type, end='\n--\n')

#II. Color-ghost
import random
class Ghost:
    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(colors)

ghost1=Ghost()
ghost2=Ghost()
ghost3=Ghost()

print(ghost1.color, ghost2.color, ghost3.color, end='\n--\n')

#III. Basic-subclasses-Adam-and-Eve
class Human:
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def create_man_and_woman():
        return [Man("Adam"), Woman("Eva")]

class Man(Human):
    pass

class Woman(Human):
    pass

adam, eve = Human.create_man_and_woman()

#IV. Classy-classes
class Person:
    def __init__(self, name:str, age:int, ):
        self.name = name
        self.age = age

    def get_info(self):
        print(f'{self.name}\'s age is {self.age}', end='\n--\n')

john = Person("John", 34)
john.get_info()

#V. Building Spheres
import math
class Sphere:
    def __init__(self, radius, mass):
        self.__radius = radius
        self.__mass = mass

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass
    
    def get_volume(self):
        return round(4/3*math.pi*self.__radius**3, 5)
    
    def get_surface_area(self):
        return round(4*math.pi*self.__radius**2, 5)
    
    def get_density(self):
        return round(self.__mass/self.get_volume(), 5)

    
ball = Sphere(2,50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density(), end='\n--\n')

#VI. Dynamic Classes
import re
def rename_class(old_class, new_name):
    if not re.match('[A-Z]{1}[A-Za-z]*', new_name):
        print('Name is incorrect')
    return type(new_name, old_class.__bases__, dict(old_class.__dict__))

class MyClass:
    pass


print('FIRST EXAMPLE: ', MyClass.__dict__, MyClass.__name__, MyClass.__bases__)

UsefulClass = rename_class(MyClass, 'UsefulClass')
print('SECOND EXAMPLE: ', UsefulClass.__dict__, UsefulClass.__name__, UsefulClass.__bases__)

SecondUsefulClass = rename_class(UsefulClass, 'SecondUsefulClass')
print('THIRD EXAMPLE: ', SecondUsefulClass.__dict__, SecondUsefulClass.__name__, SecondUsefulClass.__bases__)