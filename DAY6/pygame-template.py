import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Template")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()