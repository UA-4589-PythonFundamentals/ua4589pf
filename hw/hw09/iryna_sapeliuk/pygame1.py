from random import randint

right_number = randint(1, 100)
count = True

for i in range(1, 11):
    number = int(input("Enter a number between 1 and 100: "))
    if number < right_number:
        print("Your number is too low")
    elif number > right_number:
        print("Your number is too high")
    else:
        print("Congratulations! You've guessed the right number!")
        break

if i == 10:
    print("Sorry, you've used all your attempts. The number was:", right_number)