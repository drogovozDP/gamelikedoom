import numpy as np

PLAYER_VELOCITY = 0.2
STANDARD_CREATURE_VELOCITY = 0.5
ROTATE_VELOCITY = 1e-3
FLOOR = 0
WALL = 1
PLAYER = 2
COLOR = {
    'black': (0, 0, 0),
    'background': (0, 0, 0),
    WALL: (223, 131, 34),
    FLOOR: (20, 20, 20),
    PLAYER: (155, 0, 100),
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