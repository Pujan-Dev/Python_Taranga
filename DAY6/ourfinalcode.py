import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Survival Game")

WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

enemy_size = 40
enemy_x = 100
enemy_y = 100
enemy_speed = 2

font = pygame.font.SysFont(None, 36)
running = True
game_over = False
start_time = time.time()
high_score = 0

while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        player_x = max(0, min(WIDTH - player_size, player_x))
        player_y = max(0, min(HEIGHT - player_size, player_y))

        if enemy_x < player_x:
            enemy_x += enemy_speed
        if enemy_x > player_x:
            enemy_x -= enemy_speed
        if enemy_y < player_y:
            enemy_y += enemy_speed
        if enemy_y > player_y:
            enemy_y -= enemy_speed

        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

        if player_rect.colliderect(enemy_rect):
            game_over = True
            survival_time = int(time.time() - start_time)
            if survival_time > high_score:
                high_score = survival_time

        pygame.draw.rect(screen, BLUE, player_rect)
        pygame.draw.rect(screen, RED, enemy_rect)

        current_time = int(time.time() - start_time)
        minutes = current_time // 60
        seconds = current_time % 60
        time_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, BLACK)
        screen.blit(time_text, (10, 10))
        hs_minutes = high_score // 60
        hs_seconds = high_score % 60
        hs_text = font.render(f"High Score: {hs_minutes:02}:{hs_seconds:02}", True, BLACK)
        screen.blit(hs_text, (10, 50))

    else:
        over_text = font.render("GAME OVER", True, RED)
        survived_text = font.render(f"Survived: {minutes:02}:{seconds:02}", True, BLACK)
        screen.blit(over_text, (WIDTH//2 - 80, HEIGHT//2 - 40))
        screen.blit(survived_text, (WIDTH//2 - 80, HEIGHT//2))

    pygame.display.update()

pygame.quit()
sys.exit()
