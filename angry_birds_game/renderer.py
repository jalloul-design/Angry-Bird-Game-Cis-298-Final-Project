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


def draw_background(screen):
    screen.fill(COLOR_SKY)
    screen.blit(cloud_img, (60, 40))
    screen.blit(cloud_img, (460, 70))
    screen.blit(cloud_img, (920, 35))
    pygame.draw.rect(screen, COLOR_GROUND, (0, 620, SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_bird(screen, bird_img, x, y):
    screen.blit(bird_img, (x, y))


def draw_scene(screen, bird, obstacles, targets, bg, slingshot_held, mouse_pos):
    draw_background(screen)
    draw_bird(screen, red_bird_img, 170, 470)
    draw_bird(screen, black_bird_img, 100, 500)
    draw_bird(screen, yellow_bird_img, 50, 520)
