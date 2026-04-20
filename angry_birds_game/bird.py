# bird.py
# Owned by Sazid

import settings

class Bird:
    def __init__(self):
        self.x = settings.SLINGSHOT_X
        self.y = settings.SLINGSHOT_Y
        self.vx = 0
        self.vy = 0
        self.is_launched = False
        self.is_active = True
        self.radius = 20