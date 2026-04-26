import math

from settings import (
    GRAVITY,
    AIR_RESISTANCE,
    GROUND_Y,
    REST_SPEED_THRESHOLD,
    REST_SPIN_THRESHOLD,
    SUPPORT_TOLERANCE,
    MIN_SUPPORT_OVERLAP,
    TOPPLE_HORIZONTAL_PUSH,
    TOPPLE_SPIN_PUSH,
    TOPPLE_MAX_SIDE_SPEED,
    TOPPLE_MAX_SPIN,
)

def apply_physics_defaults(obj, mass=1.0, friction=0.3, health=1, material="wood", object_type="block"):
    obj.setdefault('vx', 0)
    obj.setdefault('vy', 0)
    obj.setdefault('angle', 0)
    obj.setdefault('angular_velocity', 0)
    obj.setdefault('mass', mass)
    obj.setdefault('friction', friction)
    obj.setdefault('health', health)
    obj.setdefault('max_health', obj['health'])
    obj.setdefault('material', material)
    obj.setdefault('kind', object_type)
    obj.setdefault('is_static', True)
    obj.setdefault('supported', True)
    obj.setdefault('state', 'idle' if object_type == 'pig' else 'resting')
    obj.setdefault('active', True)
    obj.setdefault('contact_ids', set())
    if object_type == "pig":
        obj.setdefault('radius', min(obj.get('width', 40), obj.get('height', 40)) / 2)
        obj.setdefault('is_alive', obj.get('active', True))
    return obj

def update(bird):
    if not bird.is_launched or not bird.is_active:
        return
    bird.prev_x = bird.x
    bird.prev_y = bird.y
    bird.vy += GRAVITY
    bird.vx *= AIR_RESISTANCE
    bird.vy *= AIR_RESISTANCE
    bird.x += bird.vx
    bird.y += bird.vy

    if hasattr(bird, 'angle') and hasattr(bird, 'angular_velocity'):
        bird.angle += bird.angular_velocity * (1 / 60)
        bird.angular_velocity *= 0.99

    if bird.y + bird.radius >= GROUND_Y:
        bird.y = GROUND_Y - bird.radius
        bird.vy = 0
        bird.vx = 0
        bird.is_active = False

def future_pos(bird, frames_ahead):
    x, y = bird.x, bird.y
    vx, vy = bird.vx, bird.vy
    for _ in range(frames_ahead):
        vy += GRAVITY
        vx *= AIR_RESISTANCE
        vy *= AIR_RESISTANCE
        x += vx
        y += vy
        if y + bird.radius >= GROUND_Y:
            y = GROUND_Y - bird.radius
            break
    return x, y

def get_trajectory_points(bird, num_points=30, step_frames=5):
    points = []
    x, y = bird.x, bird.y
    vx, vy = bird.vx, bird.vy
    for i in range(num_points):
        points.append((int(x), int(y)))
        for _ in range(step_frames):
            vy += GRAVITY
            vx *= AIR_RESISTANCE
            vy *= AIR_RESISTANCE
            x += vx
            y += vy
            if y + bird.radius >= GROUND_Y or (abs(vx) < 0.1 and abs(vy) < 0.1):
                y = min(y, GROUND_Y - bird.radius)
                break
    return points

def get_trajectory_from_drag(drag_x, drag_y, num_points=30, step_frames=5):
    from settings import SLINGSHOT_X, SLINGSHOT_Y, DRAG_MULTIPLIER, MAX_DRAG, GROUND_Y
    dx = max(-MAX_DRAG, min(MAX_DRAG, drag_x))
    dy = max(-MAX_DRAG, min(MAX_DRAG, drag_y))
    vx = dx * DRAG_MULTIPLIER
    vy = dy * DRAG_MULTIPLIER
    points = []
    x, y = SLINGSHOT_X, SLINGSHOT_Y
    for i in range(num_points):
        points.append((int(x), int(y)))
        for _ in range(step_frames):
            vy += GRAVITY
            vx *= AIR_RESISTANCE
            vy *= AIR_RESISTANCE
            x += vx
            y += vy
            if y + 20 >= GROUND_Y or (abs(vx) < 0.1 and abs(vy) < 0.1):
                y = min(y, GROUND_Y - 20)
                break
    return points

def apply_collision_response(obj1, obj2, collision_point):
    rel_vx = obj1['vx'] - obj2['vx']
    rel_vy = obj1['vy'] - obj2['vy']

    center1_x, center1_y = _get_center(obj1)
    center2_x, center2_y = _get_center(obj2)
    dx = center2_x - center1_x
    dy = center2_y - center1_y
    distance = math.sqrt(dx*dx + dy*dy)

    if distance == 0:
        nx, ny = 1, 0
    else:
        nx, ny = dx / distance, dy / distance

    rel_vel_along_normal = rel_vx * nx + rel_vy * ny
    if rel_vel_along_normal > 0:
        return

    restitution = 0.8
    impulse = -(1 + restitution) * rel_vel_along_normal / (1 / obj1['mass'] + 1 / obj2['mass'])
    impulse_x = impulse * nx
    impulse_y = impulse * ny

    obj1['vx'] -= impulse_x / obj1['mass']
    obj1['vy'] -= impulse_y / obj1['mass']
    obj2['vx'] += impulse_x / obj2['mass']
    obj2['vy'] += impulse_y / obj2['mass']

    r1x = collision_point[0] - center1_x
    r1y = collision_point[1] - center1_y
    r2x = collision_point[0] - center2_x
    r2y = collision_point[1] - center2_y
    torque1 = r1x * impulse_y - r1y * impulse_x
    torque2 = r2x * (-impulse_y) - r2y * (-impulse_x)

    if 'angular_velocity' in obj1:
        I1 = _get_moment_of_inertia(obj1)
        obj1['angular_velocity'] += torque1 / I1
    if 'angular_velocity' in obj2:
        I2 = _get_moment_of_inertia(obj2)
        obj2['angular_velocity'] += torque2 / I2

    tx, ty = -ny, nx
    rel_vel_tangent = rel_vx * tx + rel_vy * ty
    friction = min(obj1.get('friction', 0.3), obj2.get('friction', 0.3))
    max_friction = friction * abs(impulse)
    if abs(rel_vel_tangent) < max_friction:
        friction_impulse = -rel_vel_tangent
    else:
        friction_impulse = -max_friction * (1 if rel_vel_tangent > 0 else -1)
    friction_x = friction_impulse * tx
    friction_y = friction_impulse * ty

    obj1['vx'] -= friction_x / obj1['mass']
    obj1['vy'] -= friction_y / obj1['mass']
    obj2['vx'] += friction_x / obj2['mass']
    obj2['vy'] += friction_y / obj2['mass']

def _get_center(obj):
    if 'radius' in obj:
        return obj['x'], obj['y']
    return obj['x'] + obj.get('width', 0) / 2, obj['y'] + obj.get('height', 0) / 2

def _get_moment_of_inertia(obj):
    if 'radius' in obj:
        return max(0.5 * obj['mass'] * (obj.get('radius', 10) ** 2), 0.0001)
    width = obj.get('width', 10)
    height = obj.get('height', 10)
    return max((obj['mass'] * (width * width + height * height)) / 12, 0.0001)

def update_rotation(obj, dt=1/60):
    if 'angle' in obj and 'angular_velocity' in obj:
        obj['angle'] += obj['angular_velocity'] * dt
        obj['angular_velocity'] *= 0.99

def update_physics_object(obj, dt=1.0):
    if not obj.get('active', True):
        return

    obj['prev_x'] = obj['x']
    obj['prev_y'] = obj['y']

    if obj.get('is_static', False):
        obj['vx'] = 0
        obj['vy'] = 0
        if abs(obj.get('angular_velocity', 0)) < REST_SPIN_THRESHOLD:
            obj['angular_velocity'] = 0
        return

    if 'vy' in obj:
        obj['vy'] += GRAVITY * dt
    if 'vx' in obj:
        obj['vx'] *= AIR_RESISTANCE
    if 'vy' in obj:
        obj['vy'] *= AIR_RESISTANCE
    if 'vx' in obj:
        obj['x'] += obj['vx'] * dt
    if 'vy' in obj:
        obj['y'] += obj['vy'] * dt

    update_rotation(obj, dt)

    if 'y' in obj and obj['y'] + obj.get('height', 0) >= GROUND_Y:
        obj['y'] = GROUND_Y - obj.get('height', 0)
        fall_speed = abs(obj.get('vy', 0))
        if fall_speed > 25 and obj.get('kind') == 'pig':
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
    active_objects = [obj for obj in objects if obj.get('active', True)]
    support_data = {}

    for obj in active_objects:
        support_data[id(obj)] = _get_support_data(obj, active_objects)
        obj['supported'] = support_data[id(obj)]['center_supported']

    for obj in active_objects:
        speed = math.hypot(obj.get('vx', 0), obj.get('vy', 0))
        spin = abs(obj.get('angular_velocity', 0))
        resting_state = 'idle' if obj.get('kind') == 'pig' else 'resting'

        if support_data[id(obj)]['has_support'] and not support_data[id(obj)]['center_supported']:
            _apply_topple_bias(obj, support_data[id(obj)])
            speed = math.hypot(obj.get('vx', 0), obj.get('vy', 0))
            spin = abs(obj.get('angular_velocity', 0))

        if obj['supported'] and speed <= REST_SPEED_THRESHOLD and spin <= REST_SPIN_THRESHOLD:
            obj['is_static'] = True
            obj['vx'] = 0
            obj['vy'] = 0
            obj['angular_velocity'] = 0
            obj['state'] = resting_state
        else:
            obj['is_static'] = False
            if obj.get('state') not in ('dead', 'broken'):
                obj['state'] = 'falling'

    for obj in objects:
        if not obj.get('active', True):
            if obj.get('kind') == 'pig':
                obj['is_alive'] = False
                obj['state'] = 'dead'
            else:
                obj['state'] = 'broken'
            obj['is_static'] = False
            obj['supported'] = False

def _get_support_data(obj, active_objects):
    obj_left = obj['x']
    obj_right = obj['x'] + obj.get('width', 0)
    obj_center_x = (obj_left + obj_right) / 2

    if obj['y'] + obj.get('height', 0) >= GROUND_Y - SUPPORT_TOLERANCE:
        return {
            'has_support': True,
            'center_supported': True,
            'support_left': obj_left,
            'support_right': obj_right,
            'support_midpoint': obj_center_x,
        }

    support_left = None
    support_right = None

    for other in active_objects:
        if other is obj:
            continue
        overlap = _get_support_overlap(other, obj)
        if overlap is None:
            continue
        left, right = overlap
        if support_left is None:
            support_left = left
            support_right = right
        else:
            support_left = min(support_left, left)
            support_right = max(support_right, right)

    if support_left is None:
        return {
            'has_support': False,
            'center_supported': False,
            'support_left': None,
            'support_right': None,
            'support_midpoint': None,
        }

    return {
        'has_support': True,
        'center_supported': support_left <= obj_center_x <= support_right,
        'support_left': support_left,
        'support_right': support_right,
        'support_midpoint': (support_left + support_right) / 2,
    }

def _get_support_overlap(support, obj):
    support_top = support['y']
    obj_bottom = obj['y'] + obj.get('height', 0)
    vertical_gap = support_top - obj_bottom

    if vertical_gap < -SUPPORT_TOLERANCE or vertical_gap > SUPPORT_TOLERANCE:
        return None

    left = max(obj['x'], support['x'])
    right = min(obj['x'] + obj.get('width', 0), support['x'] + support.get('width', 0))
    if (right - left) < MIN_SUPPORT_OVERLAP:
        return None

    return left, right

def _apply_topple_bias(obj, support_data):
    support_midpoint = support_data['support_midpoint']
    if support_midpoint is None:
        return

    obj_center_x = obj['x'] + obj.get('width', 0) / 2
    half_width = max(obj.get('width', 1) / 2, 1)
    leverage = min(abs(obj_center_x - support_midpoint) / half_width, 1.0)
    direction = 1 if obj_center_x > support_midpoint else -1

    obj['vx'] = _clamp(obj.get('vx', 0) + TOPPLE_HORIZONTAL_PUSH * leverage * direction,
                       -TOPPLE_MAX_SIDE_SPEED, TOPPLE_MAX_SIDE_SPEED)
    obj['angular_velocity'] = _clamp(obj.get('angular_velocity', 0) + TOPPLE_SPIN_PUSH * leverage * direction,
                                     -TOPPLE_MAX_SPIN, TOPPLE_MAX_SPIN)

def _clamp(value, low, high):
    return max(low, min(high, value))