
class NotADayOfWeek (Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

def week_day ():
    week = {1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday', 7 : 'Sunday' }
    day = int(input('Print a day of week: '))
    if day == 1:
        print(f'It is a {week[1]}')
    elif day == 2:
        print(f'It is a {week[2]}')
    elif day == 3:
        print(f'It is a {week[3]}')
    elif day == 4:
        print(f'It is a {week[4]}')
    elif day == 5:
        print(f'It is a {week[5]}')
    elif day == 6:
        print(f'It is a {week[6]}')
    elif day == 7:
        print(f'It is a {week[7]}')
    if day >= 8:
        raise NotADayOfWeek ('It is not a day of week')

try:
    week_day()
except ValueError:
    print('Wrong data type')
except NotADayOfWeek as e:
    print(f'Handled exception: {e.message}')



