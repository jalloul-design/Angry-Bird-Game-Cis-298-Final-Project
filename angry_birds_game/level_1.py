# level_1.py
# Owner: Hussein Alsawafi
# Obstacle and target layout for level 1 (easiest - widely spaced targets, no stacking)
# level_1.py
# Owned by Hussein

def get_obstacles():
    return [
        {"x": 700, "y": 450, "width": 30, "height": 100, "active": True, 
         "vx": 0, "vy": 0, "angle": 0, "angular_velocity": 0, "mass": 10, "friction": 0.5},
        {"x": 800, "y": 430, "width": 30, "height": 120, "active": True,
         "vx": 0, "vy": 0, "angle": 0, "angular_velocity": 0, "mass": 12, "friction": 0.5},
    ]

def get_targets():
    return [
        {"x": 720, "y": 400, "width": 40, "height": 40, "active": True,
         "vx": 0, "vy": 0, "angle": 0, "angular_velocity": 0, "mass": 5, "friction": 0.3},
        {"x": 820, "y": 380, "width": 40, "height": 40, "active": True,
         "vx": 0, "vy": 0, "angle": 0, "angular_velocity": 0, "mass": 5, "friction": 0.3},
    ]