import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Jump Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dino settings
dino_width = 40
dino_height = 40
dino_x = 50
dino_y = SCREEN_HEIGHT - dino_height - 50
dino_vel_y = 0
gravity = 0.8
jump_force = -15
is_jumping = False

# Obstacle settings
obstacle_width = 20
obstacle_height = 40
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - obstacle_height - 50
obstacle_speed = 6

# Clock
clock = pygame.time.Clock()

# Main game loop
running = True
score = 0

font = pygame.font.SysFont(None, 40)

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        dino_vel_y = jump_force
        is_jumping = True

    # Dino movement
    dino_vel_y += gravity
    dino_y += dino_vel_y

    if dino_y >= SCREEN_HEIGHT - dino_height - 50:
        dino_y = SCREEN_HEIGHT - dino_height - 50
        is_jumping = False

    # Obstacle movement
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = SCREEN_WIDTH + random.randint(0, 500)
        score += 1
        obstacle_speed += 0.2  # Increase difficulty

    # Collision detection
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if dino_rect.colliderect(obstacle_rect):
        running = False

    # Draw dino
    pygame.draw.rect(screen, BLACK, dino_rect)

    # Draw obstacle
    pygame.draw.rect(screen, BLACK, obstacle_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
print(f"Game Over! Your score: {score}")
