class Human:
    def __init__(self, name):
        self.name = name

    def greet (self):
        print(f"Hi, {self.name}")

    @classmethod
    def species_info (cls):
        print("I am Homo sapiens!")

    @staticmethod
    def random_message ():
        print('Good!')
