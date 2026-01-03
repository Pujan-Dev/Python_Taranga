import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Template")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
player_x, player_y = 400, 300
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    # simulate keyboard input
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player_x -= 1
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player_x += 1
    if pygame.key.get_pressed()[pygame.K_UP]:
        player_y -= 1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player_y += 1
    # pygames.draw.rect(screen, BLUE, (x,y,width,height))

    pygame.draw.rect(screen, BLUE, (player_x, player_y, 100, 100))
    pygame.display.update()
    # screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()