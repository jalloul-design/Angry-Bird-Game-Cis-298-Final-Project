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
COLOR_UI_TITLE = (255, 210, 90)
COLOR_UI_SUBTITLE = (220, 220, 220)
COLOR_BUTTON_IDLE = (180, 70, 50)
COLOR_BUTTON_HOVER = (220, 100, 75)
COLOR_BUTTON_TEXT = (255, 255, 255)
COLOR_OVERLAY = (0, 0, 0)
COLOR_LEVEL_LOCKED = (80, 80, 90)
COLOR_LEVEL_UNLOCKED = (90, 160, 90)
COLOR_STAR_ON = (255, 215, 0)
COLOR_STAR_OFF = (70, 70, 70)

COLOR_UI_TITLE = (255, 255, 0)
COLOR_UI_SUBTITLE = (230, 230, 230)
COLOR_BUTTON_IDLE = (40, 40, 120)
COLOR_BUTTON_HOVER = (70, 70, 160)
COLOR_BUTTON_TEXT = (255, 255, 255)
COLOR_OVERLAY = (0, 0, 0, 185)
COLOR_LEVEL_UNLOCKED = (100, 220, 100)

# Level title display duration in milliseconds
LEVEL_TITLE_DURATION = 2000
