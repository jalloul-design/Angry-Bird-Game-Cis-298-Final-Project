#storing bird state, position, velocity, and if its in bounds
#sazid

from settings import SLINGSHOT_X, SLINGSHOT_Y

class Bird:
    __slots__ = ['x', 'y', 'vx', 'vy', 'prev_x', 'prev_y', 'is_launched', 'is_active', 'radius', 'mass', 'angle', 'angular_velocity', 'friction'] 
    
    def __init__(self):
        self.radius = 20 #SIZE
        self.mass = 1.0  # Mass for physics calculations
        self.angle = 0  # Rotation angle in radians
        self.angular_velocity = 0  # Rotation speed
        self.friction = 0.3  # Friction coefficient
        self.reset()

    def reset(self):
        self.x = SLINGSHOT_X
        self.y = SLINGSHOT_Y
        self.prev_x = SLINGSHOT_X
        self.prev_y = SLINGSHOT_Y
        self.vx = 0
        self.vy = 0
        self.is_launched = False
        self.is_active = True
        self.angle = 0
        self.angular_velocity = 0
    