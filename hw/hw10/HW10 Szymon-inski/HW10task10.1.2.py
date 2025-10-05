class Human:
    name = " "

    def  __init__ (self, name):
        self.name = name

    def hello (self):
        return f'Hello, {self.name}'

    def human_app (self):
        return f' The {self.name} is Homosapiens'

    @staticmethod
    def random ():
        return 'It is message'