
class WrongInt (Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def enter_age ():
    try:
         age = int(input('Enter your age: '))
         if age < 0:
             raise WrongInt('Negative input')
         if age % 2 != 0:
             print('Your age is odd')
         else: print('Your age is even')

    except ValueError:
        print('Wrong data type')
    except WrongInt as e:
        print(f'Handled exception : {e.message}')

enter_age()








