# Owned by Mira
import pygame
from pathlib import Path
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_SKY, COLOR_GROUND

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

cloud_img = pygame.image.load(str(ASSETS_DIR / "cloud_picture.png"))
cloud_img = pygame.transform.scale(cloud_img, (150, 80))
red_bird_img = pygame.image.load(str(ASSETS_DIR / "red_bird.png"))
black_bird_img = pygame.image.load(str(ASSETS_DIR / "black_bird.png"))
yellow_bird_img = pygame.image.load(str(ASSETS_DIR / "yellow_bird.png"))
red_bird_img = pygame.transform.scale(red_bird_img, (60, 60))
black_bird_img = pygame.transform.scale(black_bird_img, (60, 60))
yellow_bird_img = pygame.transform.scale(yellow_bird_img, (60, 60))

#explosion placehilders **TODO**
def trigger_explosion(x, y, obj_type="obstacle"):
    # explosion placeholder for game logic
    return

def trigger_impact(x, y):
    return


def draw_background(screen):
    screen.fill(COLOR_SKY)
    screen.blit(cloud_img, (60, 40))
    screen.blit(cloud_img, (460, 70))
    screen.blit(cloud_img, (920, 35))
    pygame.draw.rect(screen, COLOR_GROUND, (0, 620, SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_bird(screen, bird_img, x, y, angle=0):
    if angle != 0:
        # rotate bird sprite
        rotated_img = pygame.transform.rotate(bird_img, -angle * 180 / 3.14159) #logic from AI
        rect = rotated_img.get_rect(center=(x + 30, y + 30))
        screen.blit(rotated_img, rect)
    else:
        screen.blit(bird_img, (x, y))

def draw_obstacles(screen, obstacles):
    from settings import COLOR_OBSTACLE
    for obs in obstacles: # Used AI to help with this
        if obs.get("active", True):
            x, y, w, h = obs["x"], obs["y"], obs["width"], obs["height"]
            # Draw shadow
            pygame.draw.rect(screen, (max(0, COLOR_OBSTACLE[0] - 50), max(0, COLOR_OBSTACLE[1] - 50), max(0, COLOR_OBSTACLE[2] - 50)), 
                           (x + 2, y + 2, w, h))
            # Draw main obstacle
            pygame.draw.rect(screen, COLOR_OBSTACLE, (x, y, w, h))
            # Draw border
            pygame.draw.rect(screen, (max(0, COLOR_OBSTACLE[0] - 30), max(0, COLOR_OBSTACLE[1] - 30), max(0, COLOR_OBSTACLE[2] - 30)), 
                           (x, y, w, h), 2)

def draw_targets(screen, targets):
    from settings import COLOR_TARGET
    for target in targets: # Used AI to help with this
        if target.get("active", True):
            x, y, w, h = target["x"], target["y"], target["width"], target["height"]
            # Draw shadow
            pygame.draw.rect(screen, (max(0, COLOR_TARGET[0] - 50), max(0, COLOR_TARGET[1] - 50), max(0, COLOR_TARGET[2] - 50)), 
                           (x + 2, y + 2, w, h))
            # Draw main target
            pygame.draw.rect(screen, COLOR_TARGET, (x, y, w, h))
            # Draw border
            pygame.draw.rect(screen, (max(0, COLOR_TARGET[0] - 30), max(0, COLOR_TARGET[1] - 30), max(0, COLOR_TARGET[2] - 30)), 
                           (x, y, w, h), 2)


def draw_scene(screen, bird, obstacles, targets, bg, slingshot_held, mouse_pos):
    draw_background(screen)
    draw_obstacles(screen, obstacles)
    draw_targets(screen, targets)
    bird_angle = getattr(bird, 'angle', 0)
    draw_bird(screen, red_bird_img, bird.x - 30, bird.y - 30, bird_angle)
    draw_bird(screen, red_bird_img, 170, 470)
    draw_bird(screen, black_bird_img, 100, 500)
    draw_bird(screen, yellow_bird_img, 50, 520)

