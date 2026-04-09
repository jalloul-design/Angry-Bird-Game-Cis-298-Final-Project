# settings.py
# Shared by all team members
# Holds all constants: screen size, FPS, gravity, slingshot anchor, colors

# --- Hussein: Screen and game constants ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "Angry Birds"
TOTAL_LEVELS = 3

# Slingshot anchor point (x, y) on screen
SLINGSHOT_X = 200
SLINGSHOT_Y = 500

# Drag sensitivity — how fast the bird launches relative to drag distance
# Larger value = faster launch. Sazid tunes this during physics testing.
DRAG_MULTIPLIER = 0.3

# Maximum drag distance in pixels (limits launch power)
MAX_DRAG = 120

# --- Sazid: Physics constants (to be filled by Sazid) ---
GRAVITY = 0.5

# --- Mira: Color values (to be filled by Mira) ---
COLOR_SKY = (135, 206, 235)
COLOR_GROUND = (34, 139, 34)
COLOR_OBSTACLE = (139, 90, 43)
COLOR_TARGET = (80, 200, 80)
COLOR_SLINGSHOT = (101, 67, 33)
COLOR_TRAJECTORY = (255, 255, 255)
COLOR_UI_TEXT = (255, 255, 255)

# Level title display duration in milliseconds
LEVEL_TITLE_DURATION = 2000
