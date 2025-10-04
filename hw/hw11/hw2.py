def days(num):
    
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    num_of_day = int(num)

    if not (1 <= num_of_day <= 7):
        raise IndexError
    return week[num_of_day - 1]

try:
    row_str = input('Enter number of week day : ')

    print(days(row_str))

except IndexError as e:
    print(f'{e.__class__.__name__} : The week has only 7 days. Try one more time.')

except ValueError:
    print('Wrong value. I expect a number from 1 to 7. Try again.')

