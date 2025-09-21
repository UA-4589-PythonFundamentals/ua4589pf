class Employee:
    """This class contains info about new employee"""
    count = 0
    _instances = []

    def __init__(self, name=" ", salary = 100):
        Employee.count += 1
        Employee._instances.append(self)
        self.name = name
        self.salary = salary

    
    def show_info(self):
        print(f"This info is about worker: {self.name}")
        print(f"\tName: {self.name}\n\tSalary: {self.salary}")
        
    @staticmethod
    def show_employees():
        print(f"Total employees: {Employee.count}")
        if Employee._instances:
            for _ in Employee._instances:
                print(f"Name: {_.name}")
                print(f"Salary: {_.salary}")
                print("\n")
        else:
            print("There are no employees")

    @staticmethod
    def cls_info():
        print(f"This line shows from what Employee class inherits: \n\t{Employee.__base__}")
        print(f"This line shows Employee class namespace : \nt\t{Employee.__dict__}")
        print(f"this line shows Employee class name: \n\t{Employee.__name__}")
        print(f"This line shows Employee class module name: \n\t{Employee.__module__}")
        print(f"This line shows Employee class documentaion: \n\t{Employee.__doc__}")
        

    



Employee.show_employees()
e1 = Employee("John",15)
e1.show_employees()
e2 = Employee("Victro",25)
e1.show_employees()

e1.show_info()

Employee.cls_info()