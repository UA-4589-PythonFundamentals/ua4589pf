import random

def guess_the_number() -> None:
    
    secret_number = random.randint(1, 100)
    attempts = 10

    print("\033[91mWelcome to the Number Guessing Game!\033[0m")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\033[95mAttempt {attempt}/{attempts}\033[0m - Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.\n")
            continue
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            return

        if guess == secret_number:
            print(f"\033[92mCongratulations! You guessed the number in {attempt} attempts.\033[0m")
            return
        elif guess < secret_number:
            print("Too low! Try again.\n")
        else:
            print("Too high! Try again.\n")

    print(f"Sorry, you've used all {attempts} attempts.")
    print(f"The correct number was {secret_number}.")


if __name__ == "__main__":
    guess_the_number()
