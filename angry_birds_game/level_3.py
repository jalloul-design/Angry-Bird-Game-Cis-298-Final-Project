# level_3.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 3 (hardest - more targets, tighter gaps, heavy obstacles)

from source.physics import apply_physics_defaults

def get_obstacles():
    return [
        apply_physics_defaults({"x": 600, "y": 350, "width": 30, "height": 200, "active": True}, mass=15, friction=0.5, health=4),
        apply_physics_defaults({"x": 700, "y": 370, "width": 30, "height": 180, "active": True}, mass=14, friction=0.5, health=4),
        apply_physics_defaults({"x": 780, "y": 350, "width": 100, "height": 30, "active": True}, mass=8, friction=0.4, health=3),
        apply_physics_defaults({"x": 900, "y": 400, "width": 30, "height": 150, "active": True}, mass=13, friction=0.5, health=4),
    ]

def get_targets():
    return [
        apply_physics_defaults({"x": 610, "y": 300, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=2),
        apply_physics_defaults({"x": 710, "y": 320, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=2),
        apply_physics_defaults({"x": 790, "y": 300, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=2),
        apply_physics_defaults({"x": 910, "y": 350, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=2),
    ]