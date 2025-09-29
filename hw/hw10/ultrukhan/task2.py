class Human:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print(f"Hello {self.name}!")

    def species_type(self):
        return f'{self.name} is a species of "Homosapiens"'

    @staticmethod
    def arbitrary_message():
        return "Arbitrary message"