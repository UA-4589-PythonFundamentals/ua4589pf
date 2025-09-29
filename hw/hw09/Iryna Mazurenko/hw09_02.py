import pygame
import math

FPS = 60
WIDTH_DISPLAY = 600
HEIGHT_DISPLAY = 600

CENTER_X = WIDTH_DISPLAY // 2
CENTER_Y = HEIGHT_DISPLAY // 2
RADIUS = 200

RECT_W = 60
RECT_H = 40

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()

angle = 0
speed = 0.005  # speed of rotation

def draw_dotted_circle(surface, color, center, radius, segments=60):
    for i in range(segments):
        start_angle = (2 * math.pi / segments) * i
        end_angle = start_angle + 0.05  # short arc
        start_x = center[0] + radius * math.cos(start_angle)
        start_y = center[1] + radius * math.sin(start_angle)
        end_x = center[0] + radius * math.cos(end_angle)
        end_y = center[1] + radius * math.sin(end_angle)
        pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), 2)

# --- Main Loop ---
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    angle += speed
    if angle > 2 * math.pi:
        angle -= 2 * math.pi

    x = CENTER_X + RADIUS * math.cos(angle)
    y = CENTER_Y + RADIUS * math.sin(angle)

    rect_x = x - RECT_W / 2
    rect_y = y - RECT_H / 2

    screen.fill(BLUE)  # background blue
    draw_dotted_circle(screen, YELLOW, (CENTER_X, CENTER_Y), RADIUS)  #  dotted yellow path
    pygame.draw.rect(screen, YELLOW, (rect_x, rect_y, RECT_W, RECT_H))  
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()


