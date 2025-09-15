from random import randint

secret_num = randint(1, 100)
number_attempts = 10

print("Hello, i guessed random number between 1 and 100")
print("You have 10 tries to guess it")
for attempt in range(1, number_attempts +1):
    try:
        guess = int(input(f"Take a guess, attempt №{attempt}\n"))

        if guess == secret_num:
            print("Congrats, you guessed it")
            break
        elif guess < secret_num:
            print("Secret num is bigger than your guess")
        else:
            print("Secret num is less that your guess")
    except ValueError:
        print("Error! enter valid number")
else:
    print("You dont guess number. Better luck next time :(")
    print("Secret number was:", secret_num)