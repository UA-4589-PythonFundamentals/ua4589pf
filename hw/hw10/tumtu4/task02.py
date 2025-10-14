class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello {self.name}"
    
    @classmethod
    def species(cls):
        return "Homosapiens"
    
    @staticmethod
    def information():
        return "There are 8 billion people on planet Earth"
    
a = Human("Ann")
print(a.welcome_message())

print(a.species())
print(Human.species())

print(a.information())
print(Human.information())
