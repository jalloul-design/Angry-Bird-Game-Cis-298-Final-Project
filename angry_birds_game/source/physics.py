#sazid
#movement of birds; gravyity and position

from settings import GRAVITY

def update(bird):
    if not bird.is_launched or not bird.is_active: #not updating without motion
        return
    bird.vy += GRAVITY 
    #pos based on velocity
    bird.x += bird.vx 
    bird.y += bird.vy 
