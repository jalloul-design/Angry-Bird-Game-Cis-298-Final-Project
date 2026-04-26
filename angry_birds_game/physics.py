# physics.py
# Owner: Sazid

import settings

def update(bird):
    if not bird.is_launched:
        return
    bird.prev_x = bird.x
    bird.prev_y = bird.y
    bird.vy += settings.GRAVITY
    bird.vx *= settings.AIR_RESISTANCE
    bird.vy *= settings.AIR_RESISTANCE
    bird.x += bird.vx
    bird.y += bird.vy
    if bird.y >= settings.GROUND_Y:
        bird.y = settings.GROUND_Y
        bird.is_active = False

def apply_collision_response(obj1, obj2, collision_point):
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        total_mass = obj1.get("mass", 1.0) + obj2.get("mass", 1.0)
        if total_mass <= 0:
            return
        v1x = obj1.get("vx", 0)
        v1y = obj1.get("vy", 0)
        v2x = obj2.get("vx", 0)
        v2y = obj2.get("vy", 0)
        obj1["vx"] = (v1x * (obj1.get("mass", 1.0) - obj2.get("mass", 1.0)) + 2 * obj2.get("mass", 1.0) * v2x) / total_mass
        obj1["vy"] = (v1y * (obj1.get("mass", 1.0) - obj2.get("mass", 1.0)) + 2 * obj2.get("mass", 1.0) * v2y) / total_mass
    else:
        if hasattr(obj1, "vx"):
            obj1.vx *= -0.5
            obj1.vy *= -0.5