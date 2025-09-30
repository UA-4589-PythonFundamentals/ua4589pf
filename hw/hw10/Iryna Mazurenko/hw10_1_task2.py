class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return f"These species are {cls.species}."

    @staticmethod
    def arbitrary_message():
        return "Better late than never."

names = ["Iryna", "Dmytro", "Anna", "Olena", "Sergii"]

people = [Human(name) for name in names]

for person in people:
    print(person.welcome())

print(Human.get_species())
print(Human.arbitrary_message())
