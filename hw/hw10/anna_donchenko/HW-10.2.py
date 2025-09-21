#Task1
#Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball:
    def __init__(self, ball_type="regular"):
        self.ballType = ball_type

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ballType) 
print(ball2.ballType)  


#Task2
#Create a class Ghost
#Ghost objects are instantiated without any arguments.
#Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost1 = Ghost()
ghost2 = Ghost()

print(ghost1.color) 
print(ghost2.color) 


#Task3
#The creation method must return an array of length 2 containing objects (representing Adam and Eve). 
#The first object in the array should be an instance of the class Man. 
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human. 
# Your job is to implement the Human, Man and Woman classes.


class Human:
    pass

class Man(Human):
    def __str__(self):
        return "Man"

class Woman(Human):
    def __str__(self):
        return "Woman"

def create():
    return [Man(), Woman()]

#Task4
#Your task is to complete this Class, the Person class has been created. 
# You must fill in the Constructor method to accept a name as string and an age as number, 
# complete the get Info property and getInfo method/Info getter which should return johns age is 34

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"


#Task5

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
        volume = (4/3) * math.pi * self.radius**3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius**2
        return round(surface_area, 5)

    def get_density(self):
        volume = (4/3) * math.pi * self.radius**3
        density = self.mass / volume
        return round(density, 5)



#Task6

import re

def rename_class(cls, new_name):
    # Validate new class name
    if not re.fullmatch(r'[A-Z][A-Za-z0-9]*', new_name):
        raise ValueError("Invalid class name. Must start with uppercase letter and be alphanumeric.")

    # Create a new class with the new name, same base classes and attributes
    return type(new_name, cls.__bases__, dict(cls.__dict__))

