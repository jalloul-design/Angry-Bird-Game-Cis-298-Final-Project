# level_2.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 2 (medium - stacked blocks, more precise shots)

def get_obstacles():
    return [
        {"x": 650, "y": 400, "width": 30, "height": 150, "active": True},
        {"x": 750, "y": 380, "width": 30, "height": 170, "active": True},
        {"x": 850, "y": 420, "width": 30, "height": 130, "active": True},
    ]

def get_targets():
    return [
        {"x": 660, "y": 350, "width": 40, "height": 40, "active": True},
        {"x": 760, "y": 330, "width": 40, "height": 40, "active": True},
        {"x": 860, "y": 370, "width": 40, "height": 40, "active": True},
    ]