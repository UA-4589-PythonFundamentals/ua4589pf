import pygame
import sys
from random import randint

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number Game")

FONT = pygame.font.SysFont("Arial", 24)
BIG_FONT = pygame.font.SysFont("Arial", 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

secret_number = randint(1, 100)
max_attempts = 10
attempts = 0
user_input = ""
message = "Guess a number between 1 and 100"
game_over = False

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.isdigit():
                        guess = int(user_input)
                        attempts += 1
                        if guess < secret_number:
                            message = "Too low!"
                        elif guess > secret_number:
                            message = "Too high!"
                        else:
                            message = f"You guessed it! It was {secret_number}"
                            game_over = True
                    else:
                        message = "Please enter a valid number."
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    if event.unicode.isdigit():
                        user_input += event.unicode

    if attempts >= max_attempts and not game_over:
        message = f"Out of attempts! The number was {secret_number}"
        game_over = True

    # --- Render UI ---
    title_text = BIG_FONT.render("Guess the Number", True, BLACK)
    input_text = FONT.render("Your guess: " + user_input, True, BLACK)
    message_text = FONT.render(message, True, BLACK)
    attempts_text = FONT.render(f"Attempts: {attempts}/{max_attempts}", True, BLACK)

    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 30))
    screen.blit(input_text, (50, 100))
    screen.blit(message_text, (50, 150))
    screen.blit(attempts_text, (50, 200))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

