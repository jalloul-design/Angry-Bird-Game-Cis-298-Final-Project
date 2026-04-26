import pygame
from pathlib import Path
from settings import SLINGSHOT_X, SLINGSHOT_Y, DRAG_MULTIPLIER, COLOR_TRAJECTORY, MAX_DRAG, AIR_RESISTANCE
from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    COLOR_SKY,
    COLOR_GROUND,
    GRAVITY,
    GROUND_Y,
    SKY_Y,
    COLOR_OBSTACLE_WOOD,
    COLOR_OBSTACLE_GLASS,
    COLOR_OBSTACLE_STONE,
)

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

cloud_img = pygame.image.load(str(ASSETS_DIR / "cloud_picture.png"))
cloud_img = pygame.transform.scale(cloud_img, (150, 80))
red_bird_img = pygame.image.load(str(ASSETS_DIR / "red_bird.png"))
black_bird_img = pygame.image.load(str(ASSETS_DIR / "black_bird.png"))
yellow_bird_img = pygame.image.load(str(ASSETS_DIR / "yellow_bird.png"))
pig_img = pygame.image.load(str(ASSETS_DIR / "pig.png"))
slingshot_img = pygame.image.load(str(ASSETS_DIR / "slingshot.png"))
red_bird_img = pygame.transform.scale(red_bird_img, (60, 60))
black_bird_img = pygame.transform.scale(black_bird_img, (60, 60))
yellow_bird_img = pygame.transform.scale(yellow_bird_img, (60, 60))
pig_img = pygame.transform.scale(pig_img, (40, 40))
slingshot_img = pygame.transform.scale(slingshot_img, (150, 170))
activate_explosion = []

def trigger_explosion(x, y, obj_type="obstacle"):
    if obj_type == "target":
        color = (250, 200, 50)
    else:
        color = (250, 150, 100)
    recurring_explosion = {"x": x, "y": y, "color": color, "start_time": pygame.time.get_ticks()}
    activate_explosion.append(recurring_explosion)

def trigger_impact(x, y):
    new_trigger_impact = {"x": x, "y": y, "color": (200, 200, 200), "start_time": pygame.time.get_ticks()}
    activate_explosion.append(new_trigger_impact)

# Claude: How do I draw the explosions to look like real explosion in an angry bird game
def draw_explosions(screen):
    duration = 1000
    explosion_still_in_play = []

    for explosion in activate_explosion:
        time_now = pygame.time.get_ticks()
        elapsed = time_now - explosion["start_time"]

        if elapsed >= duration:
            continue

        progress = elapsed / duration
        radius = int(10 + progress * 50)
        alpha = int(255 * (1 - progress))

        size = radius * 2
        explosion_surface = pygame.Surface((size, size), pygame.SRCALPHA)

        red = explosion["color"][0]
        green = explosion["color"][1]
        blue = explosion["color"][2]
        color_with_transparency = (red, green, blue, alpha)

        pygame.draw.circle(explosion_surface, color_with_transparency, (radius, radius), radius)

        draw_x = explosion["x"] - radius
        draw_y = explosion["y"] - radius
        screen.blit(explosion_surface, (draw_x, draw_y))

        explosion_still_in_play.append(explosion)

    activate_explosion.clear()
    for explosion in explosion_still_in_play:
        activate_explosion.append(explosion)

def draw_background(screen):
    screen.fill(COLOR_SKY)
    screen.blit(cloud_img, (60, 40))
    screen.blit(cloud_img, (460, 70))
    screen.blit(cloud_img, (920, 35))
    pygame.draw.rect(screen, COLOR_GROUND, (0, 620, SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_health_bar(screen, x, y, width, health, max_health):
    if max_health <= 0:
        return
    bar_width = width
    bar_height = 6
    bar_x = x
    bar_y = y - 12
    filled_width = int(bar_width * max(0, health) / max(max_health, 1))
    pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
    pygame.draw.rect(screen, (200, 40, 40), (bar_x, bar_y, filled_width, bar_height))

def draw_bird(screen, bird_img, x, y, angle=0):
    if angle != 0:
        rotated_img = pygame.transform.rotate(bird_img, -angle * 180 / 3.14159)
        rect = rotated_img.get_rect(center=(x + 30, y + 30))
        screen.blit(rotated_img, rect)
    else:
        screen.blit(bird_img, (x, y))

def draw_pigs(screen, pigs):
    for pig in pigs:
        if pig.get("active", True):
            screen.blit(pig_img, (pig["x"], pig["y"]))

def draw_slingshot(screen):
    x = SLINGSHOT_X - 90
    y = SLINGSHOT_Y - 30
    screen.blit(slingshot_img, (x, y))

def draw_trajectory(screen, start_x, start_y, vx, vy):
    """Draw a dotted trajectory starting from the bird's actual position"""
    x = start_x
    y = start_y
    simulate_vx = vx
    simulate_vy = vy

    for i in range(15):
        for t in range(4):
            simulate_vx *= AIR_RESISTANCE   # FIX: apply air resistance so arc matches real flight
            simulate_vy *= AIR_RESISTANCE
            simulate_vy += GRAVITY
            x += simulate_vx
            y += simulate_vy

        if y > GROUND_Y or y < SKY_Y:
            break

        pygame.draw.circle(screen, COLOR_TRAJECTORY, (int(x), int(y)), 2)

def draw_obstacles(screen, obstacles):
    for obs in obstacles:
        if obs.get("active", True):
            x, y, w, h = obs["x"], obs["y"], obs["width"], obs["height"]
            color = _get_obstacle_color(obs.get("material", "wood"))
            pygame.draw.rect(screen, (max(0, color[0] - 50), max(0, color[1] - 50), max(0, color[2] - 50)),
                           (x + 2, y + 2, w, h))
            pygame.draw.rect(screen, color, (x, y, w, h))
            pygame.draw.rect(screen, (max(0, color[0] - 30), max(0, color[1] - 30), max(0, color[2] - 30)),
                           (x, y, w, h), 2)
            if obs.get('health') is not None:
                draw_health_bar(screen, x, y, w, obs['health'], obs.get('max_health', obs['health']))

def draw_targets(screen, targets):
    for target in targets:
        if target.get("active", True):
            x, y, w, h = target["x"], target["y"], target["width"], target["height"]
            if target.get('health') is not None:
                draw_health_bar(screen, x, y, w, target['health'], target.get('max_health', target['health']))

def _get_obstacle_color(material):
    if material == "glass":
        return COLOR_OBSTACLE_GLASS
    if material == "stone":
        return COLOR_OBSTACLE_STONE
    return COLOR_OBSTACLE_WOOD


def draw_scene(screen, bird, obstacles, targets, bg, slingshot_held, mouse_pos, birds_left):
    if bg is not None:
        screen.blit(bg, (0, 0))
    else:
        draw_background(screen)

    draw_slingshot(screen)
    draw_obstacles(screen, obstacles)
    draw_targets(screen, targets)
    bird_angle = getattr(bird, 'angle', 0)

    # Claude: How can I get the birds to rotate taking a hit rather than one color bird to do it
    shots_taken = 5 - birds_left
    bird_index = shots_taken % 3

    if bird_index == 0:
        current_bird_img = red_bird_img
    elif bird_index == 1:
        current_bird_img = yellow_bird_img
    else:
        current_bird_img = black_bird_img

    draw_explosions(screen)
    draw_pigs(screen, targets)

    if slingshot_held and mouse_pos is not None:
        mx, my = mouse_pos
        dx = SLINGSHOT_X - mx
        dy = SLINGSHOT_Y - my
        dx = max(-MAX_DRAG, min(MAX_DRAG, dx))
        dy = max(-MAX_DRAG, min(MAX_DRAG, dy))
        bird_draw_x = SLINGSHOT_X - dx
        bird_draw_y = SLINGSHOT_Y - dy
    else:
        bird_draw_x = bird.x
        bird_draw_y = bird.y

    draw_bird(screen, current_bird_img, bird_draw_x - 30, bird_draw_y - 30, bird_angle)

    if slingshot_held and mouse_pos is not None:
        vx = dx * DRAG_MULTIPLIER
        vy = dy * DRAG_MULTIPLIER
        # FIX: start trajectory from the bird's actual dragged position, not the slingshot anchor
        draw_trajectory(screen, bird_draw_x, bird_draw_y, vx, vy)

    else:
        bird_draw_x = bird.x
        bird_draw_y = bird.y

    draw_bird(screen, current_bird_img, bird_draw_x - 30, bird_draw_y - 30, bird_angle)

    if slingshot_held and mouse_pos is not None:
        vx = dx * DRAG_MULTIPLIER
        vy = dy * DRAG_MULTIPLIER
        draw_trajectory(screen, SLINGSHOT_X, SLINGSHOT_Y, vx, vy)
