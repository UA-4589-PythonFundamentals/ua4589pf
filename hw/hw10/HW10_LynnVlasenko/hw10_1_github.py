from pprint import pprint

# Task1. ______________________________________________________________________________________________
# Create a polygon class and a rectangle class that inherits from the polygon class 
# and finds the square of rectangle.

class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

print("---------Task1------------\n")
r = Rectangle(3, 7)
print(f"Rectangle Area: {r.area()}")
print(f"Rectangle sides: {r.sides}")
print("--------------------------\n\n")


# Task2. ______________________________________________________________________________________________
# Create a class Human, everyone has a name, 
# create a method in the class that displays a welcome message to each person. 
# Create a class method in the class that returns information that it is a species of "Homosapiens". 
# And in the class create a static method that returns an arbitrary message.

class Human:
    SPECIES = "Homosapiens"

    def __init__(self, name: str):
        self.name = name

    def welcome_message(self):
        return f"Hello {self.name}!"
    
    @classmethod
    def species(cls):
        return f"We are a species of {cls.SPECIES}"
    
    @staticmethod
    def arbitrary_message():
        return "There is just a static method here"

print("---------Task2------------\n")
lynn = Human("Lynn")
print(lynn.welcome_message())
print(lynn.species())
print(Human.species())
print(lynn.arbitrary_message())
print(Human.arbitrary_message())
print("--------------------------\n\n")


# Task3. ______________________________________________________________________________________________
# Create an employee class. Each employee has characteristics such as name and salary. 
# The class should have a counter that calculates the total number of employees, 
# as well as a method that prints the total number of employees 
# and a method that displays information about each employee in particular, namely the name and salary.
# In addition to creating a class, 
# display information about the base classes from which the employee class is inherited (__base__), 
# the class namespace (__dict__),
# the class name (__name__), 
# the module name in which the class is defined (__module__), 
# the documentation bar ( __doc__)



class Employee:

    # counter that calculates the total number of employees:
    count = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.pk = self.get_total_employee()
        Employee.count += 1
    
    @classmethod
    def get_total_employee(cls):
        """method that displays the total number of employees"""
        return cls.count


    def display_info(self):
        """method that displays information about employee - the name and salary"""
        return f"ID: {self.pk}, Employee_name: {self.name}, Salary: {self.salary}"
    

    @classmethod
    def get_class_info(cls):
        """method that display information about the class"""
        
        class_info = {
            "Base classes from which the employee class is inherited:": cls.__base__,
            "The class namespace:": cls.__dict__,
            "The class name:": cls.__name__,
            "The module name in which the class is defined:": cls.__module__,
            "The documentation bar:": cls.__doc__
        }
        pprint(class_info)


print("---------Task3------------\n")
employees = [Employee("Lynn", 3000), Employee("Anton", 5000), Employee("Bob", 2500)]

# information about employee - the name and salary:
print(employees[0].display_info())
print(employees[1].display_info())
print(employees[2].display_info())

# the total number of employees
print(f"\nTotal number of employees: {Employee.get_total_employee()}")

# information about the class
print("\n Information about the class: \n")
Employee.get_class_info()