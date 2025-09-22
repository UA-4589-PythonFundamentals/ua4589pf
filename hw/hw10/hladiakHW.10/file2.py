class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello {self.name}, welcome to the program!")

    @classmethod
    def species(cls):
        return ("Homo sapiens")

    @staticmethod
    def random_message():
        return ("Humans are awesome")


h1 = Human("Alice")
h1.welcome()

print(Human.species())
print(Human.random_message())
