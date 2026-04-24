# level_2.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 2 (medium - stacked blocks, more precise shots)

from source.physics import apply_physics_defaults

def get_obstacles():
    return [
        apply_physics_defaults({"x": 650, "y": 400, "width": 30, "height": 150, "active": True}, mass=12, friction=0.5),
        apply_physics_defaults({"x": 750, "y": 380, "width": 30, "height": 170, "active": True}, mass=14, friction=0.5),
        apply_physics_defaults({"x": 850, "y": 420, "width": 30, "height": 130, "active": True}, mass=11, friction=0.5),
    ]

def get_targets():
    return [
        apply_physics_defaults({"x": 660, "y": 350, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3),
        apply_physics_defaults({"x": 760, "y": 330, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3),
        apply_physics_defaults({"x": 860, "y": 370, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3),
    ]