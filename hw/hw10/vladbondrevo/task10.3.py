class Employee():
    num = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num += 1
        
    def calc(self):
        print(f"Total number of employees: {self.num}")
        
    def info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

a = Employee("Ben", 1000)
b = Employee("Harry", 1500)
c = Employee("Paul", 2000)
d = Employee("Tim", 2500)

a.info()
b.info()
c.info()
d.info()
d.calc()

print(Employee.__base__)
print(Employee.__dict__)    
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
