import pygame
import random

computer_choice = random.randint(1,100) 
count = 0   #This variable will be used to track how many attemtps user have made

#Setting up the game
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Number guessing Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

#This will be the text that will tell the user if he's right or wrong
base_text = f"Guess the number! You have {10-count} attempts"

#Here is the part with input box
input_text = ""
input_active = False
input_box = pygame.Rect(350,500,140,32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive


is_on = True
while is_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_on = False
        
        #Handles if program gets input from user
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False
            color = color_active if input_active else color_inactive


        if event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(input_text)
                    if guess>100 or guess < 1:
                        base_text = "Number out of range. Number is between 1 and 100"
                        input_text = ""
                    elif guess < computer_choice:
                        count += 1 
                        if count == 10:
                            base_text = f"You've failed! The number was {computer_choice}"
                            input_active = False
                        else:
                            base_text = f"Too low! Number is bigger. You have {10-count} attempts"
                        input_text = ""
                    elif guess > computer_choice:
                        count += 1 
                        if count == 10:
                            base_text = f"You've failed! The number was {computer_choice}"
                            input_active = False
                        else:
                            base_text = f"Too high! Number is lower. You have {10-count} attempts"
                        input_text = ""
                    elif guess == computer_choice:
                        base_text = f"You've got it! The number is {computer_choice}. It took {count} attempts"
                        input_text = ""
                        input_active = False
                except ValueError:
                    base_text = "Invalid input!"
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode


        
        
    screen.fill("white")
    
    #This part is needed to print text on screen
    base_text_surface = font.render(base_text, True, "black")
    screen.blit(base_text_surface, (280,20))

    #Render input text
    input_surface = font.render(input_text,True,"black")
    screen.blit(input_surface,(input_box.x + 5,input_box.y + 5))

    #Draw input box
    pygame.draw.rect(screen,color,input_box,2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()