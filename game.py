import pygame
import random

pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PLAYER_SIZE = 50
ENEMY_SIZE = 50
SPEED = 5

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger Game")

# Player Setup
player = pygame.Rect(WIDTH // 2, HEIGHT - 2 * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Enemy Setup
enemies = []


def spawn_enemy():
    x_pos = random.randint(0, WIDTH - ENEMY_SIZE)
    enemy = pygame.Rect(x_pos, 0, ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(enemy)


# Game Loop
clock = pygame.time.Clock()
running = True
spawn_timer = 0

while running:
    clock.tick(30)
    screen.fill(WHITE)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= SPEED
    if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
        player.x += SPEED

    # Enemy Movement
    if spawn_timer >= 30:  # Spawn enemy every 30 frames
        spawn_enemy()
        spawn_timer = 0
    spawn_timer += 1

    for enemy in enemies[:]:
        enemy.y += SPEED
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
        if player.colliderect(enemy):
            running = False  # Game over on collision

    # Draw Player
    pygame.draw.rect(screen, BLACK, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    pygame.display.flip()

pygame.quit()
