class AgeExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.message = msg

def check(age):
    if age < 0:
        raise AgeExcept("Age can't be negative.")
    else:
        if age % 2 == 1:
            return "Your age is odd"
        else:
            return "Your age is even"

try:
    age = int(input("Enter your age: "))
    print(check(age))
except ValueError:
    print("Enter your age as an integer")