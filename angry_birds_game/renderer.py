# Owned by Mira
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_SKY, COLOR_GROUND

cloud_img = pygame.image.load("../assets/cloud_picture.png") # ChatGPT: "Why won't the image load, even though I have it in the asset folder?" Answer " Add ". ." it will work because it goes up one folder and look for source/assets/cloud_picture.png"
cloud_img = pygame.transform.scale(cloud_img, (150, 80))  # fixed: not full screen size

def draw_background(screen):
    screen.fill(COLOR_SKY)
    screen.blit(cloud_img, (60, 40))
    screen.blit(cloud_img, (460, 70))
    screen.blit(cloud_img, (920, 35))
    pygame.draw.rect(screen, COLOR_GROUND, (0, 620, SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_scene(screen):
    draw_background(screen)


