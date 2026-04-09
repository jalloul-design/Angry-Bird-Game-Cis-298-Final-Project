# main.py
# Owner: Hussein Alsawafi
# Game loop, event polling, calls physics update and renderer each frame

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE

pygame.init()
print(f"{TITLE} — project initialized successfully. Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT} @ {FPS}fps")
pygame.quit()
