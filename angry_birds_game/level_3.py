# level_3.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 3 (hardest - more targets, tighter gaps, heavy obstacles)

def get_obstacles():
    return [
        {"x": 600, "y": 350, "width": 30, "height": 200, "active": True},
        {"x": 700, "y": 370, "width": 30, "height": 180, "active": True},
        {"x": 780, "y": 350, "width": 100, "height": 30, "active": True},
        {"x": 900, "y": 400, "width": 30, "height": 150, "active": True},
    ]

def get_targets():
    return [
        {"x": 610, "y": 300, "width": 40, "height": 40, "active": True},
        {"x": 710, "y": 320, "width": 40, "height": 40, "active": True},
        {"x": 790, "y": 300, "width": 40, "height": 40, "active": True},
        {"x": 910, "y": 350, "width": 40, "height": 40, "active": True},
    ]