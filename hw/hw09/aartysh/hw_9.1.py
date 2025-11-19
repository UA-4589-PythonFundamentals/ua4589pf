from random import randint

right_number = randint(1, 100)
attempt = 0
print("Guess the number between 1 and 100")

while attempt < 10:
    answer = int(input())
    if answer > 100 or answer < 1:
        print("Entered number is not between 1 and 100!")
        continue
    elif answer == right_number:
        print("Correct!")
        break
    elif answer > right_number:
        print("The guessed number is smaller than your guess.")
    elif answer < right_number:
        print("The guessed number is bigger than your guess.")
    attempt += 1
if attempt == 10 and answer != right_number:
    print(f"You ran out of attempts! The correct number was {right_number}.")