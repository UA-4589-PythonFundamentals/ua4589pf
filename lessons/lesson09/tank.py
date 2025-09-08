import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tank Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 12)
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
}
BALL_POS = [750, 300]
BALL_RADIUS = 30
BALL_UP = -1

TANK_POS = [100, 300]
TANK_SPEED = 5
TANK_SHELLS = []
TANK_SHELLS_SPEED = BALL_RADIUS/2
is_running = True
IS_KEYDOWN = set()

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            IS_KEYDOWN.add(event.key)
            if event.key == pygame.K_SPACE:
                TANK_SHELLS.append([TANK_POS[0] + 25, TANK_POS[1]])
                print("Fire!")
        elif event.type == pygame.KEYUP:
            IS_KEYDOWN.discard(event.key)


    screen.fill(COLORS["white"])

    for key in IS_KEYDOWN:
        if key == pygame.K_LEFT:
            if TANK_POS[0] > 0:
                TANK_POS[0] -= 5
        elif key == pygame.K_RIGHT:
            if TANK_POS[0] < 800:
                TANK_POS[0] += 5
        elif key == 1073741906:  # Up arrow key
            if TANK_POS[1] > 0:
                TANK_POS[1] -= 5
        elif key == pygame.K_DOWN:
            if TANK_POS[1] < 600:
                TANK_POS[1] += 5

    screen.fill(COLORS["white"])

    BALL_POS[1] += BALL_UP * random.randint(2, 20)
    if BALL_POS[1] + BALL_RADIUS > 600 or BALL_POS[1] - BALL_RADIUS < 0:
        BALL_UP *= -1
    pygame.draw.circle(screen, COLORS["red"], BALL_POS, BALL_RADIUS)

    for shell in TANK_SHELLS:
        shell[0] += TANK_SHELLS_SPEED
        pygame.draw.circle(screen, COLORS["black"], shell, 5)
        if (shell[0] - BALL_POS[0]) ** 2 + (shell[1] - BALL_POS[1]) ** 2 < (BALL_RADIUS) ** 2:
            print("Hit!")
            BALL_POS = [750, random.randint(50, 550)]
            TANK_SHELLS.remove(shell)
        elif shell[0] > 800:
            TANK_SHELLS.remove(shell)



    tank_rect = pygame.Rect(0, 0, 50, 30)
    tank_rect.center = TANK_POS

    screen.fill(COLORS["green"], tank_rect)
    
    pos_text = font.render(f"Position: {TANK_POS}", True, COLORS["black"])
    screen.blit(pos_text, (10, 30))
    
    pygame.display.flip()
    clock.tick(30)