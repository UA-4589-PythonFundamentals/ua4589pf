class Employee:
    """This class has information about employees"""
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    
    @classmethod
    def count_of_employees(cls):
        print(f'Total number of employees: {cls.counter}')
    
    def information(self):
        print(f"Information about employee: {self.name =}, {self.salary=}")

employee1=Employee("Ann", 10000)
employee2=Employee("Dan", 10000)
employee3=Employee("Tom", 10000)
employee4=Employee("Jack", 10000)

Employee.count_of_employees()
employee4.information()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
print(Employee.__class__)

