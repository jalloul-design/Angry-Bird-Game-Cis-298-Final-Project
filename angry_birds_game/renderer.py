import pygame
from pathlib import Path
from settings import SLINGSHOT_X, SLINGSHOT_Y, DRAG_MULTIPLIER, COLOR_TRAJECTORY, MAX_DRAG
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_SKY, COLOR_GROUND, GRAVITY, GROUND_Y, SKY_Y

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

activate_explosion = []

def trigger_explosion(x, y, obj_type="obstacle"):
    # explosion placeholder for game logic
    if obj_type == "target":
        color = (250, 200, 50)
    else:
        color = (250, 150 ,100)

    # Have the explosion occur everytime you hit an object
    recurring_explosion = {"x": x, "y": y, "color": color, "start_time": pygame.time.get_ticks()}
    activate_explosion.append(recurring_explosion)

def trigger_impact(x, y):
    # creating dust color cloud after explosion happens
    new_trigger_impact = {"x": x, "y": y, "color": (200,200,200), "start_time": pygame.time.get_ticks()}
    activate_explosion.append(new_trigger_impact)

# Claude: How do I draw the explosions to look like real explosion in an angry bird game
def draw_explosions(screen):

    # How long each explosion lasts in milliseconds
    duration = 1000

    # Make a new list for explosions that are still playing
    explosion_still_in_play = []

    for explosion in activate_explosion:
        # Check how long explosion has been going for
        time_now = pygame.time.get_ticks()
        elapsed = time_now - explosion["start_time"]

        # If it's been going too long, skip it so it disappears
        if elapsed >= duration:
            continue

        # Amination Time
        progress = elapsed / duration

        # The explosion starting size + how big it will get
        radius = int(10 + progress * 50)
        # The explosion fading out
        alpha = int(255 * (1 - progress))

        # To draw with transparency we need a separate surface
        size = radius * 2
        explosion_surface = pygame.Surface((size, size), pygame.SRCALPHA)

        # Get the color + add transparency
        red = explosion["color"][0]
        green = explosion["color"][1]
        blue = explosion["color"][2]
        color_with_transparency = (red, green, blue, alpha)

        # Draw the circle on the temporary surface
        pygame.draw.circle(explosion_surface, color_with_transparency, (radius, radius), radius)

        # Adding the surface onto the screen at the explosion's position
        draw_x = explosion["x"] - radius
        draw_y = explosion["y"] - radius
        screen.blit(explosion_surface, (draw_x, draw_y))

        # If one is still going, keep it in the new list
        explosion_still_in_play.append(explosion)

    # Replacing the old list with just the explosions still in play
    activate_explosion.clear()
    for explosion in explosion_still_in_play:
        activate_explosion.append(explosion)

def draw_background(screen):
    screen.fill(COLOR_SKY)
    screen.blit(cloud_img, (60, 40))
    screen.blit(cloud_img, (460, 70))
    screen.blit(cloud_img, (920, 35))
    pygame.draw.rect(screen, COLOR_GROUND, (0, 620, SCREEN_WIDTH, SCREEN_HEIGHT))

# health bar on top of an object
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
        # rotate bird sprite
        rotated_img = pygame.transform.rotate(bird_img, -angle * 180 / 3.14159) #logic from AI
        rect = rotated_img.get_rect(center=(x + 30, y + 30))
        screen.blit(rotated_img, rect)
    else:
        screen.blit(bird_img, (x, y))

def draw_trajectory(screen, start_x, start_y, vx, vy):
    """Draw a dotted trajectory """
    x = start_x
    y = start_y
    simulate_vx = vx
    simulate_vy = vy

    for i in range(15):
        # Space trajectory dots by 4
        for t in range(4):
            x = x + simulate_vx
            y = y + simulate_vy
            simulate_vy = simulate_vy + GRAVITY

        # If user aims the trajectory out of bounds, the trajectory disappears
        if y > GROUND_Y or y < SKY_Y:
            break

        pygame.draw.circle(screen, COLOR_TRAJECTORY, (int(x), int(y)), 2)

def draw_obstacles(screen, obstacles):
    from settings import COLOR_OBSTACLE
    for obs in obstacles: # Used AI to help with this
        if obs.get("active", True):
            x, y, w, h = obs["x"], obs["y"], obs["width"], obs["height"]
            # Draw shadow
            pygame.draw.rect(screen, (max(0, COLOR_OBSTACLE[0] - 50), max(0, COLOR_OBSTACLE[1] - 50), max(0, COLOR_OBSTACLE[2] - 50)),
                           (x + 2, y + 2, w, h))
            # Draw main obstacle
            pygame.draw.rect(screen, COLOR_OBSTACLE, (x, y, w, h))
            # Draw border
            pygame.draw.rect(screen, (max(0, COLOR_OBSTACLE[0] - 30), max(0, COLOR_OBSTACLE[1] - 30), max(0, COLOR_OBSTACLE[2] - 30)),
                           (x, y, w, h), 2)
            if obs.get('health') is not None: # health bar on obstacles
                draw_health_bar(screen, x, y, w, obs['health'], obs.get('max_health', obs['health']))

def draw_targets(screen, targets):
    from settings import COLOR_TARGET
    for target in targets: # Used AI to help with this
        if target.get("active", True):
            x, y, w, h = target["x"], target["y"], target["width"], target["height"]
            # Draw shadow
            pygame.draw.rect(screen, (max(0, COLOR_TARGET[0] - 50), max(0, COLOR_TARGET[1] - 50), max(0, COLOR_TARGET[2] - 50)),
                           (x + 2, y + 2, w, h))
            # Draw main target
            pygame.draw.rect(screen, COLOR_TARGET, (x, y, w, h))
            # Draw border
            pygame.draw.rect(screen, (max(0, COLOR_TARGET[0] - 30), max(0, COLOR_TARGET[1] - 30), max(0, COLOR_TARGET[2] - 30)),
                           (x, y, w, h), 2)
            if target.get('health') is not None: # health bar on targets
                draw_health_bar(screen, x, y, w, target['health'], target.get('max_health', target['health']))


def draw_scene(screen, bird, obstacles, targets, bg, slingshot_held, mouse_pos):
    if bg is not None:
        screen.blit(bg,(0,0)) # Claude logic in order to fix error
    else:
        draw_background(screen)

    draw_obstacles(screen, obstacles)
    draw_targets(screen, targets)
    bird_angle = getattr(bird, 'angle', 0)
    draw_bird(screen, red_bird_img, bird.x - 30, bird.y - 30, bird_angle)

    draw_bird(screen, red_bird_img, 170, 470)
    draw_bird(screen, black_bird_img, 100, 500)
    draw_bird(screen, yellow_bird_img, 50, 520)
    draw_explosions(screen)

    if slingshot_held and mouse_pos is not None:
        mx, my = mouse_pos
        dx = SLINGSHOT_X - mx
        dy = SLINGSHOT_Y - my
        # Using Hussein Function to clamp the drag
        dx = max(-MAX_DRAG, min(MAX_DRAG, dx))
        dy = max(-MAX_DRAG, min(MAX_DRAG, dy))
        vx = dx * DRAG_MULTIPLIER
        vy = dy * DRAG_MULTIPLIER
        draw_trajectory(screen, SLINGSHOT_X, SLINGSHOT_Y, vx, vy)




