class Human:
    species_name = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}")

    @classmethod
    def species(cls):
        return f"This species is {cls.species_name}"

    @staticmethod
    def message():
        return "Have a great day!"

person = Human("Vlad")
person.welcome()               
print(Human.species())         
print(Human.message())         

