import pygame
import sys

pygame.init()

WIDTH = 500 
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("РУХ прямокутника ")

rect = pygame.Rect(50,50,60,40)
speed = 5 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and reck.left > 0 :
    rect.x -= speed
if keys[pygame.K_RIGHT] and reck.right < WIDTH:
    rect.x += speed
if keys[pygame.K_UP] and reck.up > 0:
    rect.y -= speed
if keys[pygame.K_DOWN] and reck.bottom < HEIGHT:
    rect.y += speed 

screen.fill((255,255,255))
pygame.draw.rect(screen,(0,128,255),rect)
pygame.display.flip()