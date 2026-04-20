#storing bird state, position, velocity, and if its in bounds
#sazid

from settings import SLINGSHOT_X, SLINGSHOT_Y

class Bird:
    __slots__ = ['x', 'y', 'vx', 'vy', 'is_launched', 'is_active', 'radius'] 
    
    def __init__(self):
        self.radius = 20 #SIZE
        self.reset()

    def reset(self):
        self.x = SLINGSHOT_X
        self.y = SLINGSHOT_Y
        self.vx = 0
        self.vy = 0
        self.is_launched = False
        self.is_active = True
    