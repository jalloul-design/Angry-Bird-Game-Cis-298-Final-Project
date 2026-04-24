# level_1.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 1 (easiest - widely spaced targets, no stacking)
# level_1.py
# Owned by Hussein

from source.physics import apply_physics_defaults

def get_obstacles():
    return [
        apply_physics_defaults({"x": 700, "y": 450, "width": 30, "height": 100, "active": True}, mass=10, friction=0.5),
        apply_physics_defaults({"x": 800, "y": 430, "width": 30, "height": 120, "active": True}, mass=12, friction=0.5),
    ]

def get_targets():
    return [
        apply_physics_defaults({"x": 720, "y": 400, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3),
        apply_physics_defaults({"x": 820, "y": 380, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3),
    ]