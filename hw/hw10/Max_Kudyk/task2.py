class Human:
    #constructor
    def __init__(self, name):
        self.name = name
        

    #instance method
    def greet(self):
        return(f"Hello,{self.name}!")
    
    @classmethod
    def species(cls):
        return("This species is Homosapiens")
    
    @staticmethod
    def random_message():
        return("Have a nice day!")

person1 = Human("Bob")
person2 = Human("Lisa")

#instance method
print(person1.greet())
print(person2.greet())

#class method
print(Human.species())

#static method

print(Human.random_message())   
    
    
        
