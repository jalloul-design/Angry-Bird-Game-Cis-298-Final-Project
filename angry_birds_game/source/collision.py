#sazid
# collision detection and out of bounds

from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# returns the first obstacle hit or None
def check(bird, obstacle_list):
    if not bird.is_launched or not bird.is_active:
        return None

    for i in range(5):
        t = i / 4
        sx = bird.prev_x + (bird.x - bird.prev_x) * t
        sy = bird.prev_y + (bird.y - bird.prev_y) * t

        for obs in obstacle_list:
            if obs.active and _hits(sx, sy, bird.radius, obs):
                return obs

    return None


def destroy(obstacle):
    obstacle.active = False

# checks if the bird is out of bounds
def out_of_bounds(bird):
    m = 100
    return not (-m < bird.x < SCREEN_WIDTH + m and -m < bird.y < SCREEN_HEIGHT + m)

# checks if a rectangle is hit by bird
def _hits(cx, cy, radius, obs):
    nx = max(obs.x, min(cx, obs.x + obs.width))
    ny = max(obs.y, min(cy, obs.y + obs.height))
    dx, dy = cx - nx, cy - ny
    return dx * dx + dy * dy <= radius * radius