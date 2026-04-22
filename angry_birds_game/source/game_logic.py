# game_logic.py
# Owned by Hussein

import math
import settings

def handle_input(event, bird, slingshot_held, mouse_start):
    if event.type == 5:  # MOUSEBUTTONDOWN
        mx, my = event.pos
        dist = math.hypot(mx - settings.SLINGSHOT_X, my - settings.SLINGSHOT_Y)
        if dist < 40:
            return True, (mx, my)
    if event.type == 6 and slingshot_held:  # MOUSEBUTTONUP
        mx, my = event.pos
        dx = settings.SLINGSHOT_X - mx
        dy = settings.SLINGSHOT_Y - my
        dx = max(-settings.MAX_DRAG, min(settings.MAX_DRAG, dx))
        dy = max(-settings.MAX_DRAG, min(settings.MAX_DRAG, dy))
        bird.vx = dx * settings.DRAG_MULTIPLIER
        bird.vy = dy * settings.DRAG_MULTIPLIER
        bird.is_launched = True
        return False, None
    return slingshot_held, mouse_start

def check_win(targets):
    return all(not t.get("active", True) for t in targets)

def check_lose(bird, targets):
    out_of_bounds = (
        bird.x < 0 or bird.x > settings.SCREEN_WIDTH or
        bird.y > settings.SCREEN_HEIGHT
    )
    return out_of_bounds and not check_win(targets)