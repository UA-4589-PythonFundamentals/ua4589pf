from random import randint

cor_n = randint(1, 100)
attempt = 10

for i in range(attempt):
    print(f"This is attempt №{i + 1}")
    us_n = int(input("Your number: "))

    if us_n == cor_n:
        print(f"You guess the number {cor_n}. Congratulation!!!")
        break
    elif us_n < cor_n:
        print("Your number is less then riddled number.")
    elif us_n > cor_n:
        print("Your number is greater then riddled number.")
else:
    print(f"You lose! The riddle number was {cor_n}")