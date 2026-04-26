# level_1.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 1 (easiest - widely spaced targets, no stacking)

from source.physics import apply_physics_defaults

def get_obstacles():
    return [
        apply_physics_defaults({"x": 700, "y": 450, "width": 30, "height": 100, "active": True}, mass=9, friction=0.5, health=20, material="wood"),
        apply_physics_defaults({"x": 800, "y": 430, "width": 30, "height": 120, "active": True}, mass=9, friction=0.5, health=20, material="wood"),
        apply_physics_defaults({"x": 700, "y": 550, "width": 30, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        apply_physics_defaults({"x": 800, "y": 550, "width": 30, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        apply_physics_defaults({"x": 700, "y": 440, "width": 60, "height": 10, "active": True}, mass=4, friction=0.2, health=12, material="glass"),
        apply_physics_defaults({"x": 800, "y": 420, "width": 60, "height": 10, "active": True}, mass=4, friction=0.2, health=12, material="glass"),
    ]

def get_targets():
    return [
        apply_physics_defaults({"x": 720, "y": 400, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
        apply_physics_defaults({"x": 820, "y": 380, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
    ]