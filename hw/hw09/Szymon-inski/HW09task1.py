import random

mystical_num = random.randint(1, 100)


for i in range(10):
        guess = int(input('I thought of a number between 1 and 100. Try to guess it: '))
        if guess > mystical_num:
            print('The number is greater than expected. ')
        elif guess < mystical_num:
            print('The number is less than expected. ')
        elif guess == mystical_num:
            status = False
            print('Yoohoo! Y r champion!')


print('Im sorry, you are a real loser.')









