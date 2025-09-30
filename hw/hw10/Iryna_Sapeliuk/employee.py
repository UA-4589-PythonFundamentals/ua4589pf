class Employee:
    """
    A class representing an employee with name and salary attributes.
    Includes counter for total number of employees.
    """

    total_num = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_num += 1

    
    def get_details(self, name, salary):
        return f"Name: {self.name}, Salary: {self.salary}"
    
    @classmethod
    def output_total(cls):
        print(f"Total Employees: {cls.total_num}")
    
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 1400)
print(emp1.get_details(emp1.name, emp1.salary))
print(emp2.get_details(emp2.name, emp2.salary))
Employee.output_total()

print(f"Base classes (__bases__): {Employee.__bases__}")
print(f"Class namespace (__dict__): {Employee.__dict__}")
print(f"Class name (__name__): {Employee.__name__}")
print(f"Module name (__module__): {Employee.__module__}")
print(f"Documentation (__doc__): {Employee.__doc__}")