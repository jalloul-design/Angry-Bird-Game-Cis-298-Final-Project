
# Angry Birds Game - CIS 298 Final Project

A 2D physics-based game built with Python and Pygame.
You drag and release a bird from a slingshot to knock down targets across 3 levels.

## Team
- Hussein Alsawafi
- Sazid
- Mira

## How to Run
Install pygame first:
pip install pygame

Then run:
python main.py

## Controls
- Hold and drag the bird back with your mouse
- Release to launch
- Press R to restart
- Press N to go to the next level

## Commit Log

| Date | Member | Time Spent | What Was Done |
|------|--------|------------|---------------|
| April 20 | Hussein | 45 min | Added level 1, 2, and 3 layouts |
| April 21 | Hussein | 30 min | Added bird class |
| April 22 | Hussein | 1 hr | Added game_logic.py slingshot input and win/lose |
| April 23 | Hussein | 1 hr | Finished main.py game loop |
| April 23 | Hussein | 20 min | Updated README |

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


