import pygame
from random import randint

COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255),
    'black': (0,0,0)
}
pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Task1")
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 24)
text_box = pygame.Rect(80,75,100,50)
active = False
color = pygame.Color('purple')


rand_number = randint(1, 100)
counter = 10
user_input = ""
message = ""


is_running = True
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            elif event.key == pygame.K_RETURN:
                if user_input:
                    guess = int(user_input)
                    if guess == rand_number:
                        message = f"Ви виграли! Загаданим числом було {rand_number}"
                    else:
                        counter -= 1
                        if counter <= 0:
                            message = f"Ви програли! Число було {rand_number}"
                        elif guess < rand_number:
                            message = f"Загадане число більше. Спроб лишилось: {counter}"
                        else:
                            message = f"Загадане число менше. Спроб лишилось: {counter}"
                    user_input = ""

            else:
                if event.unicode.isdigit():
                    user_input+=event.unicode


    screen.fill(COLORS['white'])

    pygame.draw.rect(screen, color, text_box, 2)

    text_surface = font.render(user_input, True, COLORS['black'])
    text_rect = text_surface.get_rect(center=text_box.center)
    screen.blit(text_surface, text_rect)

    if message:
        msg_surface = font.render(message, True, COLORS['red'])
        screen.blit(msg_surface, (75, 150))

 
    pygame.display.flip()
    clock.tick(20)

print("Goodbye!")

