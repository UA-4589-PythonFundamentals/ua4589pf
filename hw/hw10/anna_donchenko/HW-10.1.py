#Task1
class Polygon:
    def __init__(self, num_sides, side_lengths):
        self.num_sides = num_sides
        self.side_lengths = side_lengths  

    def display_sides(self):
        print(f"Polygon with {self.num_sides} sides: {self.side_lengths}")


class Rectangle(Polygon):
    def __init__(self, length, width):
        side_lengths = [length, width, length, width]
        super().__init__(4, side_lengths)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



#Task2
class Human:
    species = "Homosapiens"  

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def random_message():
        return "Keep learning!"

    

#Task3
class Employee:
    """Class representing an employee with name and salary."""

    # Class variable to count total number of employees
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    # Instance method to display individual employee info
    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

    # Class method to display total number of employees
    @classmethod
    def display_employee_count(cls):
        print(f"Total Employees: {cls.employee_count}")


# --- Creating Employee instances ---
emp1 = Employee("Anna", 70000)
emp2 = Employee("David", 60000)

# Displaying info about individual employees
emp1.display_info()
emp2.display_info()

# Displaying total number of employees
Employee.display_employee_count()

# --- Class Metadata ---
print("\nClass Metadata:")
print("Base classes (__base__):", Employee.__base__)
print("Class namespace (__dict__):", Employee.__dict__)
print("Class name (__name__):", Employee.__name__)
print("Module name (__module__):", Employee.__module__)
print("Documentation (__doc__):", Employee.__doc__)



