import random

random_num = random.randint(1, 100)
attempts = 0

print("I guessed a number from 1 to 100. You have 10 attempts to guess it!")

while attempts < 10:
    guess = int(input("input number -> "))
    attempts += 1

if guss == random_num:
    print("How is that possible? Congratulations! ")
    break
elif guess < random_num:
    print("The number is higher!")
else:
    print("The number is lower!")

if attempts == 10 and guess != random_num:
    print("!GG!-> My number {random_num} ")
    
