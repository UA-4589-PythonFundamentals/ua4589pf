class Employee:
    count_employee = []

    def __init__(self, name_employee, salary_employee):
        self.name_employee = name_employee
        self.salary_employee = salary_employee
        Employee.count_employee.append(self)


    def employee_count(self):
        return len(Employee.count_employee)


    def info_employee(self):
        return f'{self.name_employee} have {self.salary_employee}'

    def class_employee_info(self):
        return Employee.__base__, Employee.__dict__, Employee.__name__, Employee.__doc__



