from random import randint

num = randint(1, 100)
tries = 10

print("I picked a random number between 1 and 100")
print("You have 10 tries to guess it")

for i in range(1, tries + 1):
    guess = int(input(f"Try №{i}\n"))
    if guess == num:
        print("Congratulations, you guessed random number")
        break
    elif guess > num:
        print("Random number is less")
    else:
        print("Random number is bigger")
else:
    print("Unfortunately, you didn't guess random number")
    print("Random number:", num)

