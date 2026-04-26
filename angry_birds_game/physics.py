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

def update_physics_object(obj, dt=1.0):
    if not obj.get('active', True):
        return

    obj['prev_x'] = obj['x']
    obj['prev_y'] = obj['y']

    if obj.get('is_static', False):
        obj['vx'] = 0
        obj['vy'] = 0
        return

    if 'vy' in obj:
        obj['vy'] += settings.GRAVITY * dt
    if 'vx' in obj:
        obj['vx'] *= settings.AIR_RESISTANCE
    if 'vy' in obj:
        obj['vy'] *= settings.AIR_RESISTANCE
    if 'vx' in obj:
        obj['x'] += obj['vx'] * dt
    if 'vy' in obj:
        obj['y'] += obj['vy'] * dt

    # Ground collision — kill pig if falling fast enough
    if obj['y'] + obj.get('height', 0) >= settings.GROUND_Y:
        obj['y'] = settings.GROUND_Y - obj.get('height', 0)
        fall_speed = abs(obj.get('vy', 0))
        if fall_speed > 3 and obj.get('kind') == 'pig':
            obj['health'] = 0
            obj['active'] = False
            obj['is_alive'] = False
            obj['state'] = 'dead'
        if 'vy' in obj:
            obj['vy'] = 0
        if 'vx' in obj:
            obj['vx'] *= 0.8
        obj['supported'] = True

def resolve_world_states(objects):
    for obj in objects:
        if not obj.get('active', True):
            continue
        at_ground = obj['y'] + obj.get('height', 0) >= settings.GROUND_Y - 5
        has_support = at_ground or _has_support_below(obj, objects)
        obj['supported'] = has_support
        if not has_support:
            obj['is_static'] = False

def _has_support_below(obj, objects):
    obj_bottom = obj['y'] + obj.get('height', 0)
    obj_left = obj['x']
    obj_right = obj['x'] + obj.get('width', 0)
    for other in objects:
        if other is obj or not other.get('active', True):
            continue
        other_top = other['y']
        if abs(other_top - obj_bottom) > 5:
            continue
        other_left = other['x']
        other_right = other['x'] + other.get('width', 0)
        overlap = min(obj_right, other_right) - max(obj_left, other_left)
        if overlap > 5:
            return True
    return False