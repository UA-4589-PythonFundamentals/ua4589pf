import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lesson 9")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
}
POINTS = []
is_running = True
while is_running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False
            print("Quit event detected")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                POINTS.append(event.pos)
            elif event.button == 3:
                if POINTS:
                    POINTS.pop()
            print(f"Mouse button {event.button} pressed at {event.pos}")
        elif event.type == pygame.KEYDOWN:
            print(f"Key {event.key} pressed")



    screen.fill(COLORS["white"])
    
    for point in POINTS:
        pygame.draw.circle(screen, COLORS["blue"], point, 5)
        text = font.render(f"{point}", True, COLORS["black"])
        screen.blit(text, (point[0] - 40, point[1] - 35))
    if len(POINTS) > 2:
        pygame.draw.polygon(screen, COLORS["red"], POINTS, 1)
    
    
    
    
    pygame.display.flip()
    clock.tick(60)

print("Goodbye!")
