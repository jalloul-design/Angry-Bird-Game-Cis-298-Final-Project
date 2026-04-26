# Angry Birds Game - CIS 298 Final Project
A 2D physics-based game built with Python and Pygame.
You drag and release a bird from a slingshot to knock down targets across 4 levels.

## Team
- Hussein Alsawafi
- Sazid Ludi
- Mira

## How to Run
Install pygame first:
pip install pygame

Then run:
cd Angry-Bird-Game-Cis-298-Final-Project
cd angry_birds_game
python main.py

## Controls
- Hold and drag the bird back with your mouse
- Release to launch
- Press R to restart
- Press N to go to the next level

## Commit Log

Hussein Alsawafi:
April 20: Added level 1, 2, and 3 layouts with obstacles and targets (45 mins)

April 21: Added bird class foundation (30 mins)

April 22: Built game_logic.py — slingshot input, win and lose logic (1 hour)

April 23: Finished main.py game loop and state management (1 hour)

April 23: Wrote initial README (20 mins)

April 24: Helped debug and fix physics settings and constants (1 hour)

April 24: Helped fix renderer — trajectory dots, slingshot rubber band, bird display (45 mins)

April 25: Helped fix UI — button wiring, menu flow, win and lose screens (1 hour)

April 26: Added welcome screen and wired all menu, hub, win, and lose buttons in main.py (1 hour)

April 26: Fixed trajectory alignment so dots match actual bird path (45 mins)

April 26: Fixed structure gravity by calling resolve_world_states each frame (1 hour)

April 26: Debugged and fixed pig fall death across both physics files (45 mins)

April 26: Designed and added level 4 layout (1 hour)

April 26: Resolved all git merge conflicts across the project (30 mins)

April 26: Updated README with full project details (20 mins)

Sazid Ludi:
April 10: Added bird class to track its state, velocity, and whether if its in bounds or not; fixed the settings spelling issue and added the source folder structure (55 mins)

April 11: Created physics file to implement gravity, added the bird movement update loop, fixed physics input, added future_pos for trajectory prediction, and added a .gitignore file (1 hour 15 mins)

April 15: Tested gravity to make sure it worked correctly and fixed an indentation issue in bird.py (20 mins)

April 22: Fixed typos and minor errors (10 mins)

April 22: Added __init__ so files under source could be imported correctly and added collision detection (45 mins)

April 22: Added some clarifying comments (10 mins)

April 22: Fixed the issue where draw_hud was only accepting one argument and added the rest (15 mins)

April 22: Fixed level selection and UI behavior (25 mins)

April 22: Removed a duplicate bird file (10 mins)

April 22: Another small typo fix (5 mins)

April 23: Added the actual movement and physics of the bird when moving and hitting objects (1 hour 15 mins)

April 23: Removed tests after finishing the physics changes (5 mins)

April 24: Created a physics helper and assigned it to each level design (35 mins)

April 24: Added health bars for objects and targets (25 mins)

April 25: Added more impacts so the bird does not stop after only one hit (40 mins)

April 25: Added supporting pillars and refined the level design to work with the new physics (35 mins)

Mira:
April 22: Built ui.py — menu, hub, win, lose, and level title screens (1 hour)

April 22: Added Button class with hover effects (30 mins)

April 23: Built renderer.py — background, slingshot, birds, obstacles, and explosions (45 mins)

April 24: Added rotating bird sprites and bird type cycling (30 mins)

April 25: Added rubber band slingshot visual and trajectory dots (30 mins)

April 26: Fixed trajectory to start from correct launch point (20 mins)