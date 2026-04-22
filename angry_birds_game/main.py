# main.py
# Owner: Hussein Alsawafi
# Game loop, event polling, calls physics update and renderer each frame

import pygame
import settings
from source import physics
from source import collision
from source import game_logic
import renderer
import ui
import level_1
import level_2
import level_3
from bird import Bird

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
    game_state = "playing"
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
            if game_state == "playing":
                slingshot_held, mouse_start = game_logic.handle_input(
                    event, bird, slingshot_held, mouse_start)
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

        if game_state == "playing":
            physics.update(bird)
            hit = collision.check(bird, obstacles + targets)
            if hit:
                collision.destroy_object(hit)
                score += 100
                bird.is_active = False
                bird.is_launched = False

            if not bird.is_active or game_logic.check_lose(bird, targets):
                birds_left -= 1
                bird = Bird()
                if birds_left <= 0 and not game_logic.check_win(targets):
                    game_state = "lose"

            if game_logic.check_win(targets):
                game_state = "win"

        bg = bg_images[current_level] if current_level < len(bg_images) else None
        renderer.draw_scene(screen, bird, obstacles, targets, bg,
                            slingshot_held, mouse_pos if slingshot_held else None)
        ui.draw_hud(screen, score, birds_left, current_level + 1)

        if show_title and pygame.time.get_ticks() - title_timer < settings.LEVEL_TITLE_DURATION:
            ui.draw_level_title(screen, current_level + 1)
        else:
            show_title = False

        if game_state == "win":
            ui.draw_win(screen)
        elif game_state == "lose":
            ui.draw_lose(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()