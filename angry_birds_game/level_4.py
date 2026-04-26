# level_4.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 4 (hardest - more targets, tighter gaps, heavy obstacles)

from source.physics import apply_physics_defaults

def get_obstacles():
    return [
        # Stone bases on ground
        apply_physics_defaults({"x": 650, "y": 550, "width": 80, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        apply_physics_defaults({"x": 780, "y": 550, "width": 80, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        apply_physics_defaults({"x": 910, "y": 550, "width": 80, "height": 70, "active": True}, mass=14, friction=0.6, health=28, material="stone"),
        # Wide wood pillars on top of stone
        apply_physics_defaults({"x": 650, "y": 350, "width": 80, "height": 200, "active": True}, mass=10, friction=0.5, health=24, material="wood"),
        apply_physics_defaults({"x": 780, "y": 370, "width": 80, "height": 180, "active": True}, mass=10, friction=0.5, health=24, material="wood"),
        apply_physics_defaults({"x": 910, "y": 390, "width": 80, "height": 160, "active": True}, mass=10, friction=0.5, health=24, material="wood"),
        # Wide glass roofs
        apply_physics_defaults({"x": 640, "y": 340, "width": 100, "height": 10, "active": True}, mass=4, friction=0.2, health=12, material="glass"),
        apply_physics_defaults({"x": 770, "y": 360, "width": 100, "height": 10, "active": True}, mass=4, friction=0.2, health=12, material="glass"),
        apply_physics_defaults({"x": 900, "y": 380, "width": 100, "height": 10, "active": True}, mass=4, friction=0.2, health=12, material="glass"),
    ]

def get_targets():
    return [
        # pig y = glass roof y - 40
        apply_physics_defaults({"x": 665, "y": 300, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
        apply_physics_defaults({"x": 795, "y": 320, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
        apply_physics_defaults({"x": 925, "y": 340, "width": 40, "height": 40, "active": True}, mass=5, friction=0.3, health=18, material="pig", object_type="pig"),
    ]