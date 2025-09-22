class Human:
    species = "Homosapiens"

    def __init__(self,name = "John"):
        self.name = name
        self.display_name()


    def display_name(self):
        print(f"Welcome, {self.name}")

    def give_info(self):
        return f"{self.name} belongs to {self.species}"
    
    @staticmethod
    def arbitrary_text():
        print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat." \
        " Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur." \
        " Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


h = Human(input("Enter your name: "))
h1 = Human("Dima")
h2 = Human("C3PO")

print(h.give_info())

h.arbitrary_text()
Human.arbitrary_text