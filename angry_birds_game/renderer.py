# Owned by Mira
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_SKY, COLOR_GROUND

cloud_img = pygame.image.load("../assets/cloud_picture.png") # ChatGPT: "Why won't the image load, even though I have it in the asset folder?" Answer " Add ". ." it will work because it goes up one folder and look for source/assets/cloud_picture.png"
cloud_img = pygame.transform.scale(cloud_img, (150, 80))  # fixed: not full screen size
red_bird_img = pygame.image.load("../assets/red_bird.png")
black_bird_img = pygame.image.load("../assets/black_bird.png")
yellow_bird_img = pygame.image.load("../assets/yellow_bird.png")
red_bird_img = pygame.transform.scale(red_bird_img, (60, 60))
black_bird_img = pygame.transform.scale(black_bird_img, (60, 60))
yellow_bird_img = pygame.transform.scale(yellow_bird_img, (60, 60))


def draw_background(screen):
    screen.fill(COLOR_SKY)
    screen.blit(cloud_img, (60, 40))
    screen.blit(cloud_img, (460, 70))
    screen.blit(cloud_img, (920, 35))
    pygame.draw.rect(screen, COLOR_GROUND, (0, 620, SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_bird(screen,bird_img, x,y):
    screen.blit(bird_img, (x,y))

def draw_scene(screen):
    draw_background(screen)
    draw_bird(screen,red_bird_img,170,470)
    draw_bird(screen,black_bird_img,100, 500)
    draw_bird(screen,yellow_bird_img,50,520)


