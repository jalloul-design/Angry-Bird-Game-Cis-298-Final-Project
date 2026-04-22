# Owned By Mira
# ui.py - menu, level select, win, loss, and level title screens

import pygame
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, TOTAL_LEVELS, LEVEL_TITLE_DURATION,
    COLOR_UI_TEXT, COLOR_UI_TITLE, COLOR_UI_SUBTITLE,
    COLOR_BUTTON_IDLE, COLOR_BUTTON_HOVER, COLOR_BUTTON_TEXT,
    COLOR_OVERLAY, COLOR_LEVEL_UNLOCKED, COLOR_SKY,
)


# Claude: How can I get my text to be more organized and centered on the screen
def draw_text_in_the_center(screen, text, size, y, color= COLOR_UI_TEXT):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    x = (SCREEN_WIDTH - surface.get_width()) // 2
    screen.blit(surface, (x, y))


class Button:
    def __init__(self, x, y, width, height, label, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.action = action

    def draw(self, screen):
        # Claude: How can I make my button show when the user is hovering over it
        mouse_movement = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_movement):
            color = COLOR_BUTTON_HOVER
        else:
            color = COLOR_BUTTON_IDLE

        pygame.draw.rect(screen, color, self.rect, border_radius=20)
        pygame.draw.rect(screen, COLOR_UI_TEXT, self.rect, width=2, border_radius=20)

        # Put the label text on top of the button
        font = pygame.font.Font(None, 36)
        text = font.render(self.label, True, COLOR_BUTTON_TEXT)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def mouse_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


# Claude: when person wins or loses a level how can I get the background to become transparent like an actual game
def draw_transparent_background_for_levels(screen):
    transparent_background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    transparent_background.fill((0, 0, 0, 185))
    screen.blit(transparent_background, (0, 0))


def draw_menu(screen):
    screen.fill(COLOR_SKY)

    draw_text_in_the_center(screen, "Welcome To Angry Birds", 120, 180, COLOR_UI_TITLE)
    draw_text_in_the_center(screen, "CIS 298 Final Project", 30, 280, COLOR_UI_SUBTITLE)

    # Make the two menu buttons
    start_button = Button(520, 400, 240, 60, "Start", "goto_hub")
    quit_button = Button(520, 480, 240, 60, "Quit", "quit_game")

    start_button.draw(screen)
    quit_button.draw(screen)

    return [start_button, quit_button]


def draw_hud(screen):
    screen.fill(COLOR_SKY)
    draw_text_in_the_center(screen, "Start A Level", 80, 60, COLOR_UI_TITLE)

    buttons = []
    level_box_size = 150
    gap = 40
    start_x = 410
    start_y = 210

    for i in range(TOTAL_LEVELS):
        level_number = i + 1
        x = start_x + i * (level_box_size + gap)  # Got the Calculation From Claude
        y = start_y
        rect = pygame.Rect(x, y, level_box_size, level_box_size)

        # Drawing The Level Options With Green Color
        pygame.draw.rect(screen, COLOR_LEVEL_UNLOCKED, rect, border_radius=20)
        pygame.draw.rect(screen, COLOR_SKY, rect, width=2, border_radius=20)

        # Inserting Level Number Inside Level Box
        font = pygame.font.Font(None, 65)
        label = font.render(str(level_number), True, COLOR_BUTTON_TEXT)
        label_rect = label.get_rect(center=rect.center)
        screen.blit(label, label_rect)

        # Button For Level
        level_button = Button(x, y, level_box_size, level_box_size, "", "play_level_" + str(level_number))
        buttons.append(level_button)

    # Creating A Back Button Option
    back_button = Button(40, SCREEN_HEIGHT - 90, 170, 60, "Go Back", "goto_menu")
    back_button.draw(screen)
    buttons.append(back_button)

    return buttons


def draw_level_title(screen, level_number, start):
    # Claude: How do I get the level to display when user selects which level they want to play before starting the game
    elapsed = pygame.time.get_ticks() - start
    if elapsed >= LEVEL_TITLE_DURATION:
        return False

    draw_transparent_background_for_levels(screen)
    draw_text_in_the_center(screen, "Level " + str(level_number), 120, SCREEN_HEIGHT // 2 - 60, COLOR_UI_TITLE)
    return True


def draw_win(screen, level_number, last_level=False):
    draw_transparent_background_for_levels(screen)
    draw_text_in_the_center(screen, "Level Cleared!", 90, 200, COLOR_UI_TITLE)
    draw_text_in_the_center(screen, "Level " + str(level_number), 40, 270, COLOR_UI_SUBTITLE)

    buttons = []

    if last_level:
        # Since this is a demo and we're only going up to level 3, lead the user back to either the menu or they can replay
        replay_button = Button(450, 410, 170, 60, "Replay Level", "play_level_" + str(level_number))
        menu_button = Button(650, 410, 170, 60, "Go To Menu", "goto_menu")
        replay_button.draw(screen)
        menu_button.draw(screen)
        buttons.append(replay_button)
        buttons.append(menu_button)
        draw_text_in_the_center(screen, "WOOHOO! You have completed all the levels!", 40, 490, COLOR_UI_TITLE)
    else:
        # If it is not the last level
        replay_button = Button(400, 410, 170, 60, "Replay Level", "play_level_" + str(level_number))
        menu_button = Button(590, 410, 170, 60, "Go To Menu", "goto_menu")
        next_button = Button(780, 410, 170, 60, "Next Level", "play_level_" + str(level_number + 1))
        replay_button.draw(screen)
        menu_button.draw(screen)
        next_button.draw(screen)
        buttons.append(replay_button)
        buttons.append(menu_button)
        buttons.append(next_button)

    return buttons


def draw_losses(screen, level_number):
    draw_transparent_background_for_levels(screen)
    draw_text_in_the_center(screen, "Level Failed", 90, 200, COLOR_UI_TITLE)
    draw_text_in_the_center(screen, "Level " + str(level_number) + " failed", 50, 280, COLOR_UI_SUBTITLE)
    draw_text_in_the_center(screen, "Do you want to try again?", 36, 350, COLOR_UI_TEXT)

    restart_button = Button(450, 430, 170, 60, "Restart", "play_level_" + str(level_number))
    menu_button = Button(650, 430, 170, 60, "Go To Menu", "goto_menu")
    restart_button.draw(screen)
    menu_button.draw(screen)

    return [restart_button, menu_button]





