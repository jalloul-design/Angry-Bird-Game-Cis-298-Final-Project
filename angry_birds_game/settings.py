# settings.py
# Shared by all team members
# Holds all constants: screen size, FPS, gravity, slingshot anchor, colors

# --- Hussein: Screen and game constants ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "Angry Birds"
TOTAL_LEVELS = 4

# Slingshot anchor point (x, y) on screen
SLINGSHOT_X = 200
SLINGSHOT_Y = 500

# Drag sensitivity — how fast the bird launches relative to drag distance
# Larger value = faster launch. Sazid tunes this during physics testing.
DRAG_MULTIPLIER = 0.3

# Maximum drag distance in pixels (limits launch power)
MAX_DRAG = 120

# Ground level (y coordinate where ground starts)
GROUND_Y = 620
SKY_Y = 0

# --- Sazid: Physics constants (to be filled by Sazid) ---
GRAVITY = 0.4
AIR_RESISTANCE = 0.99  # Velocity multiplier per frame

# --- Mira: Color values (to be filled by Mira) ---
COLOR_SKY = (135, 206, 235)
COLOR_GROUND = (34, 139, 34)
COLOR_OBSTACLE = (139, 90, 43) 
COLOR_OBSTACLE_WOOD = (139, 90, 43) # Brown 
COLOR_OBSTACLE_GLASS = (150, 220, 255) # Light blue 
COLOR_OBSTACLE_STONE = (115, 115, 125) # Gray 
COLOR_TARGET = (80, 200, 80)
COLOR_SLINGSHOT = (101, 67, 33)
COLOR_TRAJECTORY = (255, 0, 0)

# UI text colors
COLOR_UI_TEXT = (255, 255, 255)
COLOR_UI_TITLE = (255, 210, 90)
COLOR_UI_SUBTITLE = (220, 220, 220)

# Button colors
COLOR_BUTTON_IDLE = (180, 70, 50)
COLOR_BUTTON_HOVER = (220, 100, 75)
COLOR_BUTTON_TEXT = (255, 255, 255)

# Overlay for win/loss screens
COLOR_OVERLAY = (0, 0, 0)

# Level select tile colors
COLOR_LEVEL_LOCKED = (80, 80, 90)
COLOR_LEVEL_UNLOCKED = (90, 160, 90)
# Level title display duration in milliseconds
LEVEL_TITLE_DURATION = 2000

#keeps track of how many times bird hit structure or object; damage calculation help here
DAMAGE_MULTIPLIER = 4.0
FALL_DAMAGE_MULTIPLIER = 0.6
MIN_IMPACT_THRESHOLD = 6.0
PIG_MEDIUM_IMPACT = 14.0
PIG_LARGE_IMPACT = 36.0

MATERIAL_RESISTANCE = { # higher means more resistance to damage
    "glass": 5.0,
    "wood": 10.0,
    "stone": 22.0,
    "pig": 7.0,
}

REST_SPEED_THRESHOLD = 0.75
REST_SPIN_THRESHOLD = 0.08
SUPPORT_TOLERANCE = 6
MIN_SUPPORT_OVERLAP = 10

SCORE_BLOCK_BREAK = 100
SCORE_PIG_POP = 500

# limits how many at once get hit
BIRD_MAX_DAMAGE_HITS = 2
BIRD_POST_HIT_SPEED_MULTIPLIER = 0.6

# makes sure no floating structures
TOPPLE_HORIZONTAL_PUSH = 0.35
TOPPLE_SPIN_PUSH = 0.02
TOPPLE_MAX_SIDE_SPEED = 3.0
TOPPLE_MAX_SPIN = 0.18
