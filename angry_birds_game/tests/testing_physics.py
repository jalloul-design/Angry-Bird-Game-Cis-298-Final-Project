from source.bird import Bird
import settings
from source import physics

b = Bird()
b.vx = 5
b.vy = -10
b.is_launched = True


for i in range(10):
    physics.update(b)
    print(f"After {i+1} frames: x={b.x:.2f}, y={b.y:.2f}, vx={b.vx:.2f}, vy={b.vy:.2f}")

