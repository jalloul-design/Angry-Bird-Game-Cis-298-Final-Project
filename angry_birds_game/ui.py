# Owned By Mira
import pygame

def draw_menu(screen):
    font = pygame.font.Font(None,50)
    text = font.render("Welcome to Angry Birds!!", True, (255, 255, 255))
    screen.blit(text, (250, 200))