# level_3.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 3 (hardest - more targets, tighter gaps, heavy obstacles)

from source.physics import apply_physics_defaults

def get_obstacles():
    return [
        apply_physics_defaults({"x": 600, "y": 350, "width": 30, "height": 200, "active": True}, mass=10, friction=0.5, health=24, material="wood"),
        apply_physics_defaults({"x": 700, "y": 370, "width": 30, "height": 180, "active": True}, mass=10, friction=0.5, health=24, material="wood"),
        apply_physics_defaults({"x": 900, "y": 400, "width": 30, "height": 150, "active": True}, mass=10, friction=0.5, health=24, material="wood"),
        apply_physics_defaults({"x": 600, "y": 550, "width": 30, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        apply_physics_defaults({"x": 700, "y": 550, "width": 30, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        apply_physics_defaults({"x": 900, "y": 550, "width": 30, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        apply_physics_defaults({"x": 600, "y": 340, "width": 60, "height": 10, "active": True}, mass=4, friction=0.2, health=12, material="glass"),
        apply_physics_defaults({"x": 700, "y": 360, "width": 60, "height": 10, "active": True}, mass=4, friction=0.2, health=12, material="glass"),
        apply_physics_defaults({"x": 900, "y": 390, "width": 60, "height": 10, "active": True}, mass=4, friction=0.2, health=12, material="glass"),
        apply_physics_defaults({"x": 780, "y": 350, "width": 100, "height": 30, "active": True}, mass=5, friction=0.2, health=16, material="glass"),
        apply_physics_defaults({"x": 780, "y": 380, "width": 20, "height": 170, "active": True}, mass=8, friction=0.5, health=18, material="wood"),
        apply_physics_defaults({"x": 860, "y": 380, "width": 20, "height": 170, "active": True}, mass=8, friction=0.5, health=18, material="wood"),
        apply_physics_defaults({"x": 780, "y": 550, "width": 20, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        apply_physics_defaults({"x": 860, "y": 550, "width": 20, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
    ]

def get_targets():
    return [
        apply_physics_defaults({"x": 610, "y": 300, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
        apply_physics_defaults({"x": 710, "y": 320, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
        apply_physics_defaults({"x": 790, "y": 310, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
        apply_physics_defaults({"x": 910, "y": 350, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
    ]
