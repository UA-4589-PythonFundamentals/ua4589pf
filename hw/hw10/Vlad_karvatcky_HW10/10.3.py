class loyee:
    count = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 
        loyee.count += 1

    def count_display (self):
        print("loyees : {loyee.sount}")
    
    def info_display (self):
        print("name: {self.name}, salary: {self.salary}")

em1 = loyee("Vlad",4000)
em2 = loyee("Bill",5000)

em1.info_display()
em2.info_display()
em1.count_display()
em2.count_display()

print("Base classes:", loyee.__base__)
print("Class namespace:", loyee.__dict__)
print("Class name:", loyee.__name__)
print("Module name:", loyee.__module__)
print("Documentation:", loyee.__doc__)

