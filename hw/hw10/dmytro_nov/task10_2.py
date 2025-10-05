#Regular Ball Super Ball
# class Ball(object):
#     # your code goes here
#     def __init__(self,ball_type = None):
#         self.ball_type = "regular" if not ball_type else ball_type
        
#Color Ghost
# import random
# 'class Ghost(object):
#     colors = ["white","yellow","purple","red"]
    
#     def __init__(self):
#         self.color = random.choice(Ghost.colors)'

#Basic subclasses - Adam and Eve

# class Human:
#     def __init__(self):
#         pass
    
# class Man(Human):
#     def __init__(self):
#         super().__init__()
#         pass
    
# class Woman(Human):
#     def __init__(self):
#         super().__init__()
#         pass
    

# def God(humans = None):
#     if humans is None:
#         humans = []
#     adam = Man()
#     eve = Woman()
#     humans.append(adam)
#     humans.append(eve)
#     return humans
        
# Classy Classes

# class Person:
#     def __init__(self,name,age):
#         self.info = f"{name}s age is {age}"

# Building Spheres

# import math

# class Sphere(object):
    
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
        
#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         volume = (4/3) * math.pi * self.get_radius()**3
#         return round(volume, 5)
    
#     def get_surface_area(self):
#         surface_area = 4 * math.pi * self.get_radius()**2
#         return round(surface_area, 5)
        
#     def get_density(self):
#         if self.get_mass():
#             density = self.get_mass()/self.get_volume()
#             return round(density, 5)
#         else:
#             return None
        
#Python's Dynamic Classes #1

# def class_name_changer(cls, new_name):
#     if new_name.isalnum() and new_name[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         cls.__name__ = new_name
#     else:
#         raise Exception