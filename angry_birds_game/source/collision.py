#sazid
# collision detection and out of bounds

from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .physics import apply_collision_response

# returns only brand new hits so the bird can keep moving after the first collision
def check(bird, obstacle_list):
    if not bird.is_launched or not bird.is_active:
        bird.contact_ids.clear()
        return []

    # keeps only the objects the bird is touching right now
    current_contacts = {}
    new_hits = []

    for obs in obstacle_list:
        if not obs.get("active", True):
            continue

        collision_point = _first_collision_point(bird, obs)
        if collision_point is None:
            continue

        obs_id = id(obs)
        current_contacts[obs_id] = obs
        # if the bird is still overlapping the same object dont damage it again yet
        if obs_id in bird.contact_ids:
            continue

        # only bounce and count damage when the contact first starts
        bird_dict = {
            'x': bird.x, 'y': bird.y, 'vx': bird.vx, 'vy': bird.vy,
            'mass': getattr(bird, 'mass', 1.0),
            'angle': getattr(bird, 'angle', 0),
            'angular_velocity': getattr(bird, 'angular_velocity', 0),
            'friction': getattr(bird, 'friction', 0.3),
            'radius': bird.radius
        }

        apply_collision_response(bird_dict, obs, collision_point)

        # Update bird with new velocities and rotation
        bird.vx = bird_dict['vx']
        bird.vy = bird_dict['vy']
        if hasattr(bird, 'angle'):
            bird.angle = bird_dict['angle']
        if hasattr(bird, 'angular_velocity'):
            bird.angular_velocity = bird_dict['angular_velocity']

        new_hits.append(obs)

    # once the bird leaves an object it can hit it again later from a new angle
    bird.contact_ids = set(current_contacts)
    return new_hits

# destroys an object based on its health insteaed of insta
def destroy(obstacle, damage=1):
    if obstacle.get("health") is not None:
        obstacle["health"] = max(0, obstacle["health"] - damage)
        if obstacle["health"] <= 0:
            obstacle["active"] = False
    else:
        obstacle["active"] = False

# checks if the bird is out of bounds
def out_of_bounds(bird):
    m = 100
    return not (-m < bird.x < SCREEN_WIDTH + m and -m < bird.y < SCREEN_HEIGHT + m)

# checks if a rectangle is hit by bird
def _hits(cx, cy, radius, obs):
    nx = max(obs["x"], min(cx, obs["x"] + obs["width"]))
    ny = max(obs["y"], min(cy, obs["y"] + obs["height"]))
    dx, dy = cx - nx, cy - ny
    return dx * dx + dy * dy <= radius * radius

# checks along the birds path so fast shots still catch the first contact point
def _first_collision_point(bird, obs):
    for i in range(5):
        t = i / 4
        sx = bird.prev_x + (bird.x - bird.prev_x) * t
        sy = bird.prev_y + (bird.y - bird.prev_y) * t
        if _hits(sx, sy, bird.radius, obs):
            return sx, sy
    return None
