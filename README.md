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

Mira Jalloul:
April 3: Created the GitHub repository and made the initial commit to start the project (5 mins)

April 10: Created the ui.py and renderer.py files, added a basic draw_menu function in ui.py, and added a placeholder draw_scene function in renderer.py to set up the structure (30 mins)

April 14: Created the assets folder, added the cloud image, and built the draw_background function in renderer.py to fill the sky, draw clouds, and draw the ground. Also fixed a small UI file issue where the test variable was not matching settings.py (1 hour)

April 20: Wrote the draw_bird function in renderer.py, loaded and scaled the red, black, and yellow bird images, and uploaded the bird PNG assets to the assets folder (1 hour)

April 21: Built out the full UI for the project — wrote draw_menu, draw_hub, draw_win, draw_losses, and draw_level_title in ui.py. Added the Button class with hover state and click detection, the draw_text_in_the_center helper, and the draw_transparent_background_for_levels overlay. Also tweaked the styling of the bird drawing to match the visual feel of the game (3 hours)

April 22: Renamed draw_hub to draw_hud after Sazid pointed out the name conflict, and pulled in teammates' changes to keep my branch synced (45 mins)

April 23: Pulled in updates from Hussein and Sazid and made small adjustments to keep the renderer compatible with their changes (30 mins)

April 24: Added the draw_trajectory function in renderer.py to show a dotted preview of the bird's flight path while the player aims, tuned the trajectory dot color so it stands out on the sky, and built the explosion system (trigger_explosion, trigger_impact, and draw_explosions) so destroyed objects produce a fading expanding circle effect (1 hour 15 mins)

April 25: Added the pig PNG to the assets folder, replaced the green-rectangle target rendering with a draw_pigs function, designed the slingshot graphic, and wired the birds_left parameter through the renderer so it knows which bird type to display in the win, lose, and playing states. Also implemented the bird rotation system so each shot uses a different bird color (red, yellow, black) (1 hour 30 mins)

April 26: Made the bird visually move with the slingshot during drag and release at the launch point, removed the queued decorative birds that were cluttering the scene, helped refine level design with supporting pillars, and fixed the trajectory display so it shows as a single line of dots instead of two overlapping lines (2 hours)
