#sazid
# collision detection and out of bounds

import math

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    DAMAGE_MULTIPLIER,
    FALL_DAMAGE_MULTIPLIER,
    MIN_IMPACT_THRESHOLD,
    PIG_MEDIUM_IMPACT,
    PIG_LARGE_IMPACT,
    BIRD_MAX_DAMAGE_HITS,
    BIRD_POST_HIT_SPEED_MULTIPLIER,
    MATERIAL_RESISTANCE,
    SCORE_BLOCK_BREAK,
    SCORE_PIG_POP,
)
from .physics import apply_collision_response

def check(bird, obstacle_list):
    if not bird.is_launched or not bird.is_active:
        bird.contact_ids.clear()
        return []

    current_contacts = {}
    events = []

    for obs in obstacle_list:
        if not obs.get("active", True):
            continue

        collision_point = _first_collision_point(bird, obs)
        if collision_point is None:
            continue

        obs_id = id(obs)
        current_contacts[obs_id] = obs
        if obs_id in bird.contact_ids:
            continue

        bird_dict = _bird_to_dict(bird)
        impulse = _calculate_impulse(bird_dict, obs)
        apply_collision_response(bird_dict, obs, collision_point)
        _update_bird_from_dict(bird, bird_dict)

        bird.vx *= BIRD_POST_HIT_SPEED_MULTIPLIER
        bird.vy *= BIRD_POST_HIT_SPEED_MULTIPLIER

        if bird.hit_count >= BIRD_MAX_DAMAGE_HITS:
            continue

        bird.hit_count += 1
        event = _apply_damage_event(obs, bird_dict, impulse, collision_point)
        if event is not None:
            events.append(event)

    bird.contact_ids = set(current_contacts)
    return events

def check_environment_collisions(obstacles, targets):
    active_objects = [obj for obj in obstacles + targets if obj.get("active", True)]
    current_contacts = {id(obj): set() for obj in active_objects}

    for obj in active_objects:
        obj.setdefault("contact_ids", set())

    block_events = _process_object_pairs(
        active_objects,
        current_contacts,
        lambda obj1, obj2: obj1.get("kind") == "block" and obj2.get("kind") == "block",
    )
    pig_events = _process_object_pairs(
        active_objects,
        current_contacts,
        lambda obj1, obj2: "pig" in (obj1.get("kind"), obj2.get("kind")),
    )

    for obj in obstacles + targets:
        if obj.get("active", True):
            obj["contact_ids"] = current_contacts.get(id(obj), set())
        else:
            obj["contact_ids"] = set()

    return block_events, pig_events

def destroy(obstacle, damage=1):
    if obstacle.get("health") is not None:
        obstacle["health"] = max(0, obstacle["health"] - damage)
        if obstacle["health"] <= 0:
            _deactivate_object(obstacle)
    else:
        _deactivate_object(obstacle)

def out_of_bounds(bird):
    m = 100
    return not (-m < bird.x < SCREEN_WIDTH + m and -m < bird.y < SCREEN_HEIGHT + m)

def _process_object_pairs(active_objects, current_contacts, pair_filter):
    events = []

    for i in range(len(active_objects)):
        obj1 = active_objects[i]
        for j in range(i + 1, len(active_objects)):
            obj2 = active_objects[j]
            if not obj1.get("active", True) or not obj2.get("active", True):
                continue
            if not pair_filter(obj1, obj2):
                continue

            overlap_box = _get_overlap_box(obj1, obj2)
            if overlap_box is None:
                continue

            obj1_id = id(obj1)
            obj2_id = id(obj2)
            current_contacts[obj1_id].add(obj2_id)
            current_contacts[obj2_id].add(obj1_id)

            _separate_objects(obj1, obj2, overlap_box)

            if obj2_id in obj1["contact_ids"] or obj1_id in obj2["contact_ids"]:
                continue

            collision_point = _get_overlap_center(overlap_box)
            impulse_on_obj1 = _calculate_impulse(obj2, obj1)
            impulse_on_obj2 = _calculate_impulse(obj1, obj2)

            apply_collision_response(obj1, obj2, collision_point)

            event1 = _apply_damage_event(obj1, obj2, impulse_on_obj1, collision_point)
            if event1 is not None:
                events.append(event1)

            event2 = _apply_damage_event(obj2, obj1, impulse_on_obj2, collision_point)
            if event2 is not None:
                events.append(event2)

    return events

def _apply_damage_event(target, source, impulse, collision_point):
    damage = _calculate_damage(target, source, impulse)
    if damage <= 0:
        return None

    target["health"] = max(0, target.get("health", 0) - damage)
    target["is_static"] = False
    if target.get("state") not in ("dead", "broken"):
        target["state"] = "falling"

    destroyed = target["health"] <= 0
    if destroyed:
        _deactivate_object(target)

    center_x, center_y = _get_object_center(target)
    return {
        "target": target,
        "impulse": impulse,
        "damage": damage,
        "destroyed": destroyed,
        "score": _get_score_value(target, destroyed),
        "impact_point": collision_point,
        "center": (center_x, center_y),
    }

# damage calculation, score calc based on damage and object, destruction
def _calculate_damage(target, source, impulse):
    if impulse < MIN_IMPACT_THRESHOLD:
        return 0

    if target.get("kind") == "pig" and source.get("kind") == "pig":
        return 0

    resistance = MATERIAL_RESISTANCE.get(target.get("material", "wood"), MATERIAL_RESISTANCE["wood"])
    damage_multiplier = DAMAGE_MULTIPLIER
    if source.get("kind") != "bird":
        damage_multiplier *= FALL_DAMAGE_MULTIPLIER

    damage = impulse * damage_multiplier / resistance

    if target.get("kind") == "pig":
        if impulse >= PIG_LARGE_IMPACT:
            return target.get("health", 0)
        if impulse < PIG_MEDIUM_IMPACT:
            damage *= 0.6

    return damage

# impulse = momentum change
def _calculate_impulse(source, target):
    relative_velocity = math.hypot(
        source.get("vx", 0) - target.get("vx", 0),
        source.get("vy", 0) - target.get("vy", 0),
    )
    return relative_velocity * max(source.get("mass", 1.0), 0.0001)

def _get_score_value(target, destroyed):
    if not destroyed:
        return 0
    if target.get("kind") == "pig":
        return SCORE_PIG_POP
    return SCORE_BLOCK_BREAK

# dead pigs
def _deactivate_object(obj):
    obj["active"] = False
    obj["contact_ids"] = set()
    obj["supported"] = False
    obj["is_static"] = False

    if obj.get("kind") == "pig":
        obj["is_alive"] = False
        obj["state"] = "dead"
    else:
        obj["state"] = "broken"

# limit damage
def _bird_to_dict(bird):
    return {
        "x": bird.x,
        "y": bird.y,
        "vx": bird.vx,
        "vy": bird.vy,
        "mass": getattr(bird, "mass", 1.0),
        "angle": getattr(bird, "angle", 0),
        "angular_velocity": getattr(bird, "angular_velocity", 0),
        "friction": getattr(bird, "friction", 0.3),
        "radius": bird.radius,
        "kind": "bird",
    }

def _update_bird_from_dict(bird, bird_dict):
    bird.vx = bird_dict["vx"]
    bird.vy = bird_dict["vy"]
    if hasattr(bird, "angle"):
        bird.angle = bird_dict["angle"]
    if hasattr(bird, "angular_velocity"):
        bird.angular_velocity = bird_dict["angular_velocity"]

def _hits(cx, cy, radius, obs):
    nx = max(obs["x"], min(cx, obs["x"] + obs["width"]))
    ny = max(obs["y"], min(cy, obs["y"] + obs["height"]))
    dx, dy = cx - nx, cy - ny
    return dx * dx + dy * dy <= radius * radius

def _first_collision_point(bird, obs):
    for i in range(5):
        t = i / 4
        sx = bird.prev_x + (bird.x - bird.prev_x) * t
        sy = bird.prev_y + (bird.y - bird.prev_y) * t
        if _hits(sx, sy, bird.radius, obs):
            return sx, sy
    return None

# works against overlap and makes sure two items are not going through eachother
def _get_overlap_box(obj1, obj2):
    left = max(obj1["x"], obj2["x"])
    top = max(obj1["y"], obj2["y"])
    right = min(obj1["x"] + obj1["width"], obj2["x"] + obj2["width"])
    bottom = min(obj1["y"] + obj1["height"], obj2["y"] + obj2["height"])

    if left >= right or top >= bottom:
        return None

    return left, top, right - left, bottom - top

def _get_overlap_center(overlap_box):
    left, top, width, height = overlap_box
    return left + width / 2, top + height / 2

def _get_object_center(obj):
    return obj["x"] + obj["width"] / 2, obj["y"] + obj["height"] / 2

def _separate_objects(obj1, obj2, overlap_box):
    _, _, overlap_width, overlap_height = overlap_box
    if overlap_width <= 0 or overlap_height <= 0:
        return

    obj1_center_x, obj1_center_y = _get_object_center(obj1)
    obj2_center_x, obj2_center_y = _get_object_center(obj2)

    inverse_mass_1 = 1 / max(obj1.get("mass", 1), 0.0001)
    inverse_mass_2 = 1 / max(obj2.get("mass", 1), 0.0001)
    total_inverse_mass = inverse_mass_1 + inverse_mass_2
    if total_inverse_mass <= 0:
        return

    extra_push = 0.1
    if overlap_width < overlap_height:
        push_amount = overlap_width + extra_push
        direction = -1 if obj1_center_x < obj2_center_x else 1
        obj1["x"] += direction * push_amount * (inverse_mass_1 / total_inverse_mass)
        obj2["x"] -= direction * push_amount * (inverse_mass_2 / total_inverse_mass)
    else:
        push_amount = overlap_height + extra_push
        direction = -1 if obj1_center_y < obj2_center_y else 1
        obj1["y"] += direction * push_amount * (inverse_mass_1 / total_inverse_mass)
        obj2["y"] -= direction * push_amount * (inverse_mass_2 / total_inverse_mass)