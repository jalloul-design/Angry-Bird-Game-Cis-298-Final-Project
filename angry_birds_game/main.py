# main.py
# Owner: Hussein Alsawafi
# Game loop, event polling, calls physics update and renderer each frame

import pygame
import random
import settings
from source import physics
from source import collision
from source import game_logic
import renderer
import ui
import level_1
import level_2
import level_3
from source import bird as bird_module
from source.bird import Bird

LEVELS = [level_1, level_2, level_3]

def load_level(index):
    level = LEVELS[index]
    return level.get_obstacles(), level.get_targets(), Bird()

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()

    current_level = 0
    obstacles, targets, bird = load_level(current_level)
    score = 0
    birds_left = 5
    slingshot_held = False
    mouse_start = None
    game_state = "menu"   # <-- FIX: start at menu, not "playing"
    shake_timer = 0
    hub_buttons = []
    menu_buttons = []
    title_timer = pygame.time.get_ticks()
    show_title = True

    bg_images = []
    for i in range(1, 4):
        try:
            img = pygame.image.load(f"assets/background_{i}.png")
            img = pygame.transform.scale(img, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
            bg_images.append(img)
        except:
            bg_images.append(None)

    while True:
        clock.tick(settings.FPS)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # --- MENU state ---
            if game_state == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
                for button in menu_buttons:
                    if button.mouse_clicked(event):
                        if button.action == "goto_hub":
                            game_state = "hub"
                        elif button.action == "quit_game":
                            pygame.quit()
                            return

            # --- HUB state ---
            if game_state == "hub" and event.type == pygame.MOUSEBUTTONDOWN:
                for button in hub_buttons:
                    if button.mouse_clicked(event):
                        if button.action.startswith("play_level_"):
                            selected_level = int(button.action.split("play_level_")[1]) - 1
                            current_level = selected_level
                            obstacles, targets, bird = load_level(current_level)
                            score = 0
                            birds_left = 5
                            game_state = "playing"
                            show_title = True
                            title_timer = pygame.time.get_ticks()
                            break
                        elif button.action == "goto_menu":
                            game_state = "menu"

            # --- PLAYING state ---
            if game_state == "playing":
                slingshot_held, mouse_start = game_logic.handle_input(
                    event, bird, slingshot_held, mouse_start)

            # --- WIN / LOSE state ---
            if game_state in ("win", "lose"):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        current_level = 0
                        obstacles, targets, bird = load_level(current_level)
                        score = 0
                        birds_left = 5
                        game_state = "playing"
                        show_title = True
                        title_timer = pygame.time.get_ticks()
                    if event.key == pygame.K_n and game_state == "win":
                        if current_level < len(LEVELS) - 1:
                            current_level += 1
                            obstacles, targets, bird = load_level(current_level)
                            birds_left = 5
                            game_state = "playing"
                            show_title = True
                            title_timer = pygame.time.get_ticks()

                # Handle win/lose button clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    win_lose_buttons = win_lose_button_list if 'win_lose_button_list' in dir() else []
                    for button in win_lose_button_list if 'win_lose_button_list' in locals() else []:
                        if button.mouse_clicked(event):
                            if button.action.startswith("play_level_"):
                                selected_level = int(button.action.split("play_level_")[1]) - 1
                                current_level = selected_level
                                obstacles, targets, bird = load_level(current_level)
                                score = 0
                                birds_left = 5
                                game_state = "playing"
                                show_title = True
                                title_timer = pygame.time.get_ticks()
                            elif button.action == "goto_menu":
                                game_state = "menu"

        # ======== DRAW SECTION ========

        if game_state == "menu":
            menu_buttons = ui.draw_menu(screen)

        elif game_state == "hub":
            hub_buttons = ui.draw_hub(screen, score, birds_left, current_level + 1)
            show_title = False

        elif game_state == "playing":
            physics.update(bird)
            for obj in obstacles + targets:
                physics.update_physics_object(obj)

            hit = collision.check(bird, obstacles + targets)
            if hit:
                renderer.trigger_impact(bird.x, bird.y)
                center_x = hit["x"] + hit["width"] // 2
                center_y = hit["y"] + hit["height"] // 2
                obj_type = "target" if hit in targets else "obstacle"
                renderer.trigger_explosion(center_x, center_y, obj_type)
                collision.destroy(hit)
                score += 100
                bird.is_active = False
                bird.is_launched = False
                shake_timer = 10

            if not bird.is_active or game_logic.check_lose(bird, targets):
                from settings import GROUND_Y
                if bird.y + 20 >= GROUND_Y - 5:
                    renderer.trigger_impact(bird.x, bird.y)
                birds_left -= 1
                bird = Bird()
                if birds_left <= 0 and not game_logic.check_win(targets):
                    game_state = "lose"

            if game_logic.check_win(targets):
                game_state = "win"

            bg = bg_images[current_level] if current_level < len(bg_images) else None

            if shake_timer > 0:
                shake_x = random.randint(-8, 8)
                shake_y = random.randint(-8, 8)
                shake_timer -= 1
            else:
                shake_x, shake_y = 0, 0

            screen.fill((0, 0, 0))
            temp_surface = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
            renderer.draw_scene(temp_surface, bird, obstacles, targets, bg,
                                slingshot_held, mouse_pos if slingshot_held else None, birds_left)
            screen.blit(temp_surface, (shake_x, shake_y))
            ui.draw_hud(screen, score, birds_left, current_level + 1)

            if show_title and pygame.time.get_ticks() - title_timer < settings.LEVEL_TITLE_DURATION:
                ui.draw_level_title(screen, current_level + 1, title_timer)
            else:
                show_title = False

        else:
            bg = bg_images[current_level] if current_level < len(bg_images) else None
            renderer.draw_scene(screen, bird, obstacles, targets, bg,
                                slingshot_held, mouse_pos if slingshot_held else None, birds_left)
            ui.draw_hud(screen, score, birds_left, current_level + 1)

        if game_state == "win":
            win_lose_button_list = ui.draw_win(screen, current_level + 1, current_level == len(LEVELS) - 1)
        elif game_state == "lose":
            win_lose_button_list = ui.draw_losses(screen, current_level + 1)

        pygame.display.flip()

if __name__ == "__main__":
    main()