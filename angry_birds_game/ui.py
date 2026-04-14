# Owned By Mira
import pygame
from settings import COLOR_UI_TEXT, SCREEN_WIDTH

def draw_menu(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Welcome to Angry Birds!!", True, COLOR_UI_TEXT)
    x = (SCREEN_WIDTH - text.get_width()) // 2
    screen.blit(text, (x, 200))