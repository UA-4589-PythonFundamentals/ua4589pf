class Employee:
    """Basic class of employees"""
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    
    def total_num(self):
        print(f"Total number of employees: {self.counter}")
    
    def full_info(self):
        print(f"Name: {self.name}, salary: {self.salary}.")

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
