class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    @classmethod
    def show_total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")
    
    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


emp1 = Employee("John", 5000)
emp2 = Employee("Bob", 7000)
emp3 = Employee("Alice", 4000)

Employee.show_total_employees()

Employee.employee_info(emp1)
Employee.employee_info(emp2)
Employee.employee_info(emp3)

print("\nClass info:")
print("Base classes:", Employee.__base__)
print("Namespace (__dict__):", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)


        