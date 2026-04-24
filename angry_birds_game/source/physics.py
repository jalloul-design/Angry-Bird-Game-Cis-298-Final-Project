from settings import GRAVITY, AIR_RESISTANCE, GROUND_Y

def apply_physics_defaults(obj, mass=1.0, friction=0.3): # added this helper to avoid rewriting in every lvl design
    # ensure a physics object has the required motion and collision fields
    obj.setdefault('vx', 0)
    obj.setdefault('vy', 0)
    obj.setdefault('angle', 0)
    obj.setdefault('angular_velocity', 0)
    obj.setdefault('mass', mass)
    obj.setdefault('friction', friction)
    return obj

def update(bird):
    if not bird.is_launched or not bird.is_active:
        return
    # store previous position for collision detection
    bird.prev_x = bird.x
    bird.prev_y = bird.y
    bird.vy += GRAVITY
    bird.vx *= AIR_RESISTANCE
    bird.vy *= AIR_RESISTANCE
    bird.x += bird.vx
    bird.y += bird.vy

    # update rotation
    if hasattr(bird, 'angle') and hasattr(bird, 'angular_velocity'):
        bird.angle += bird.angular_velocity * (1 / 60)
        bird.angular_velocity *= 0.99

    # ground collision
    if bird.y + bird.radius >= GROUND_Y:
        bird.y = GROUND_Y - bird.radius
        bird.vy = 0
        bird.vx = 0
        bird.is_active = False

# future position of bird after a number of frames
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

# trajectory points for visualization
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

# trajectory from drag for aiming guide
def get_trajectory_from_drag(drag_x, drag_y, num_points=30, step_frames=5):
    from settings import SLINGSHOT_X, SLINGSHOT_Y, DRAG_MULTIPLIER, MAX_DRAG, GROUND_Y
    
    # Clamp drag like in game_logic.py
    dx = max(-MAX_DRAG, min(MAX_DRAG, drag_x))
    dy = max(-MAX_DRAG, min(MAX_DRAG, drag_y))
    
    # Initial velocity based on drag
    vx = dx * DRAG_MULTIPLIER
    vy = dy * DRAG_MULTIPLIER
    
    #starting point is slingshot anchor
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
            # Stop if hits ground 
            if y + 20 >= GROUND_Y or (abs(vx) < 0.1 and abs(vy) < 0.1):  # 20 is bird radius
                y = min(y, GROUND_Y - 20)
                break
    return points

# realistic collision response with momentum transfer and torque
def apply_collision_response(obj1, obj2, collision_point):
    import math

    # relative velocity
    rel_vx = obj1['vx'] - obj2['vx']
    rel_vy = obj1['vy'] - obj2['vy']

    # collision normal direction
    dx = obj2['x'] - obj1['x']
    dy = obj2['y'] - obj1['y']
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

    # torque from collision force
    r1x = collision_point[0] - obj1['x']
    r1y = collision_point[1] - obj1['y']
    r2x = collision_point[0] - obj2['x']
    r2y = collision_point[1] - obj2['y']
    torque1 = r1x * impulse_y - r1y * impulse_x
    torque2 = r2x * (-impulse_y) - r2y * (-impulse_x)

    if 'radius' in obj1:
        I1 = 0.5 * obj1['mass'] * (obj1.get('radius', 10) ** 2)
        obj1['angular_velocity'] += torque1 / I1
    if 'radius' in obj2:
        I2 = 0.5 * obj2['mass'] * (obj2.get('radius', 10) ** 2)
        obj2['angular_velocity'] += torque2 / I2

    # friction impulse
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

# update object rotation based on angular velocity
def update_rotation(obj, dt=1/60):
    if 'angle' in obj and 'angular_velocity' in obj:
        obj['angle'] += obj['angular_velocity'] * dt
        obj['angular_velocity'] *= 0.99

# update a physics object position and rotation
def update_physics_object(obj, dt=1/60):
    if not obj.get('active', True):
        return

    obj['prev_x'] = obj['x']
    obj['prev_y'] = obj['y']

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
        if 'vy' in obj:
            obj['vy'] = 0
        if 'vx' in obj:
            obj['vx'] *= 0.8
