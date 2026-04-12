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

#future position
# **TODO**: Mira: use this and add UI that shows the trajectory
def future_pos(bird, frames_ahead): 
    x, y = bird.x, bird.y
    vx, vy = bird.vx, bird.vy
    for _ in range(frames_ahead):
        vy += GRAVITY
        x += vx
        y += vy
    return x, y