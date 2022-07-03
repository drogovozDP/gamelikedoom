import numpy as np

WIDTH = 800
HEIGHT = 600
WALL_HEIGHT = 50
RAY_LENGTH = 400
RAY_COUNT = 80
RAY_RATE = 80
PLAYER_VELOCITY = 4
STANDARD_CREATURE_VELOCITY = 0.5
ROTATE_VELOCITY = 1e-1
FLOOR = 0
WALL = 1
PLAYER = 2
RAY = 'ray'
COLOR = {
    'black': (0, 0, 0),
    'background': (0, 0, 0),
    WALL: (223, 131, 34),
    FLOOR: (20, 20, 20),
    PLAYER: (155, 0, 100),
    RAY: (255, 255, 0)
}

LEVELS = {
    'lvl1': np.array(
        [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]
    )
}