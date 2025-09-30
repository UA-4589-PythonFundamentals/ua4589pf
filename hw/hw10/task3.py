class Employee:
    """An Employee class with a name and salary, maintains a common counter"""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
    
    @classmethod
    def employee_counter(cls):
        return cls.count
    
    def inform(self):
        return [f'Name : {self.name}', f'Salary is {self.salary}']


e = Employee("Bohdan", 2000)


print("BaseClass   :", Employee.__base__)
print("NameSpace   :", Employee.__dict__)
print("ClassName   :", Employee.__name__)
print("Module      :", Employee.__module__)
print("DocString   :", Employee.__doc__)
