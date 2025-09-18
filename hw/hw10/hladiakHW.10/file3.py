class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def total_employees(self):
        print(f"Total employees: {Employee.count}")

    def info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


e1 = Employee("Alice", 5000)
e2 = Employee("Bob", 7000)

e1.info()
e2.info()
e1.total_employees()


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
