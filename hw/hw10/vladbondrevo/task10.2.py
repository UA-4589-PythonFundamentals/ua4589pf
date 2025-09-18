class Human():
    def __init__(self, name):
        self.name = name
        
    def welcome(self):
        print(f"Hey, welcome {self.name}!")

    @classmethod    
    def info(cls):
        return "This is HomoSapiens"
        
    @staticmethod
    def message():
        return "That is static method"


a = Human("Robert")
a.welcome()

print(Human.info())
print(Human.message())
