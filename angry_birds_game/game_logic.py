# game_logic.py
# Owner: Hussein Alsawafi
# Drag input, velocity scaling, win condition, lose condition, level progression

import math
from settings import SLINGSHOT_X, SLINGSHOT_Y, DRAG_MULTIPLIER, MAX_DRAG

# Tracks whether the player is currently dragging the bird
dragging = False
drag_pos = (SLINGSHOT_X, SLINGSHOT_Y)


def handle_mouse_down(event, bird):
    """Called on MOUSEBUTTONDOWN. Start drag if player clicks near the bird."""
    global dragging, drag_pos
    bx, by = bird.x, bird.y
    mx, my = event.pos
    if math.hypot(mx - bx, my - by) <= 30:
        dragging = True
        drag_pos = event.pos


def handle_mouse_motion(event):
    """Called on MOUSEMOTION. Update drag position while button is held."""
    global drag_pos
    if dragging:
        drag_pos = event.pos


def handle_mouse_up(event, bird):
    """Called on MOUSEBUTTONUP. Calculate and apply launch velocity to the bird."""
    global dragging, drag_pos
    if not dragging:
        return
    dragging = False

    mx, my = event.pos
    dx = SLINGSHOT_X - mx
    dy = SLINGSHOT_Y - my

    # Cap the drag distance so the bird can't be over-powered
    distance = math.hypot(dx, dy)
    if distance > MAX_DRAG:
        scale = MAX_DRAG / distance
        dx *= scale
        dy *= scale

    bird.vx = dx * DRAG_MULTIPLIER
    bird.vy = dy * DRAG_MULTIPLIER
    bird.is_launched = True

    print(f"Bird launched — vx: {bird.vx:.2f}  vy: {bird.vy:.2f}")


def get_drag_pos():
    """Returns current drag position so renderer can draw the rubber band."""
    return drag_pos


def is_dragging():
    """Returns True while the player is holding the drag."""
    return dragging


def check_win(targets):
    """Returns True when all targets have been destroyed."""
    return all(not t.is_active for t in targets)


def check_lose(birds_remaining, targets):
    """Returns True when no birds are left and targets still exist."""
    return birds_remaining <= 0 and not check_win(targets)
