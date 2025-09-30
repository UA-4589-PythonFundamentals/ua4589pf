class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}! It's a pleasure to see you today."
    
    species = "Homosapiens"
    @classmethod
    def get_species(cls):

        return f"This is a species of {cls.species}"
    
    @staticmethod
    def arbitrary_message():
        return "Bye! See you later!"
    
human1 = Human("John")
human2 = Human("Alice")

print(human1.greet())
print(Human.get_species())
print(human2.greet())
print(Human.get_species())
print(Human.arbitrary_message())