The `main.py` script is the core of a 2D game developed using Pygame. This script integrates various components and controls the game logic. It involves player interaction, enemy spawning, bullet mechanics, power-ups, and collision detection.

## Modules and Imports

- `pygame`: Main library used for game development.
- `random`: Used for generating random numbers, essential for enemy spawning.
- `player`: Custom module for the player object.
- `enemy`: Custom module for enemy objects.
- `particles`: Custom module for particle effects.
- `bullet`: Custom module for bullet mechanics.
- `powerUp`: Custom module for power-up functionalities.
- `hud`: Custom module for the heads-up display (HUD).

## Constants and Global Variables

- `WIDTH`, `HEIGHT`: Dimensions of the game window.
- `DIMENSION`: Tuple combining `WIDTH` and `HEIGHT`.
- `FPS`: Frames per second, controlling the game's frame rate.
- `WHITE`, `BLACK`: Color constants.
- `AMMO`: Initial ammo count.
- `NUMBER`: Used in enemy spawning logic.
- `dead`: Boolean flag to check if the player is dead.
- `EXPLOSION`: Sound effect for explosions.

## Game Initialization

- Pygame and font initialization.
- Creation of the game window, clock, player, and HUD objects.
- `enemySpawnerTimer`, `particles`, `gameRunning`, `gameStart`: Variables to manage game states.

## Functions

1. **`draw(user, enemiesList, bullets, powerUps)`**: Renders the game screen, including players, enemies, bullets, and power-ups.

2. **`playerMove(user, keys)`**: Handles player movement based on keyboard inputs.

3. **`shoot(event, bulletsList)`**: Manages bullet shooting mechanics.

4. **`handleEnemy(user, enemyList, score)`**: Spawns and updates enemies based on game conditions.

5. **`handleBullets(bullets)`**: Updates bullet positions and handles their removal.

6. **`checkCollision(entity1, entity2)`**: Checks for collisions between two entities.

7. **`playerEnemyCollision(enemiesList, enemy)`**: Handles collision between player and enemy.

8. **`bulletEnemyCollision(enemiesList, enemy, powerUpsList, bulletsList, bullet)`**: Manages collisions between bullets and enemies, including score update and power-up spawning.

9. **`checkIfDie()`**: Checks if the player's health is depleted and updates the game state.

## Main Game Loop

The `main()` function contains the game loop, which continuously updates the game state, processes user inputs, handles collisions, and renders the game screen.

## Execution

The script runs the main game loop if it is the main module being executed.

## Running the Game

To run and play the game developed in the `main.py` script, follow these steps:

### Prerequisites

1. **Python Installation**: Ensure you have Python installed on your system. Python 3.x is recommended. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Pygame Library**: The game requires the Pygame library. Install it using pip, Python's package installer. Run the following command in your terminal or command prompt:
```bash
pip install pygame
```

3. **Game Assets**: Make sure all required game assets (images, sounds, etc.) are in the correct directory, typically in an `assets` folder in the same directory as your script. For example, the `EXPLOSION` sound is loaded from `"assets/explosion.mp3"`.

4. **Custom Modules**: The game depends on several custom modules (`player`, `enemy`, `particles`, `bullet`, `powerUp`, `hud`). Ensure these files (`player.py`, `enemy.py`, etc.) are present in the same directory as `main.py`.

### Running the Game

1. **Open Terminal/Command Prompt**: Navigate to the directory where `main.py` and its associated modules and assets are located.

2. **Execute the Script**: Run the game by executing the `main.py` script with Python. Use the following command:
```bash
python3 main.py
```
