import random 

rand = random.randint(1,100)

for a in range(10):
    num = int(input(f'Hello, you have {10 - a} tries Enter your num : '))
    if num == rand:
        print(f"Congratulations! You've guessed it in {a + 1} tries!")
        break
    elif a == 9:
        print("You've used all your tries. Better luck next time!")
    elif num > rand:
        print("Your number is greater than the target. Try again :)")
    elif num < rand:
        print("Your number is less than the target. Try again :)")