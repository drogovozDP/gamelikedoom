from engine.game_objects import GameObject
from engine.consts import *
from engine.math_functions import *
import numpy as np


class Entity(GameObject):
    def __init__(self, game_engine, x, y, color):
        super().__init__(game_engine, x, y, color)
        self.radius = self.game_engine.graphic.cell_size // 3
        self.shape = create_circle_shape(x, y, self.radius, 10)
        self.velocity = STANDARD_CREATURE_VELOCITY
        self.rotate_velocity = ROTATE_VELOCITY
        self.direction = np.array([1, 0, 1])
        self.vision = self._create_rays()

    def rotate(self, kfc):
        a = kfc * ROTATE_VELOCITY
        R = get_rotate_matrix(a, self.direction[0], self.direction[1])
        self.direction = R @ self.direction
        self.vision = self._create_rays()

    def move(self, movement):
        dx, dy, _ = movement * self.direction  # Crate shift with direction
        M = get_move_matrix(dx, dy)  # Create shift matrix
        shape = self.shape.copy()  # Shift current shape to check collision
        for i, dot in enumerate(self.shape):
            shape[i] = dot @ M
        if self.collision(shape):  # Return if collision returns True
            return
        self.shape = shape.copy()  # Set new coordinates for the shape
        self.x, self.y, _ = np.array([self.x, self.y, 1]) @ M  # set a new center
        for i, ray in enumerate(self.vision):  # move a rays
            self.vision[i] = ray @ M

    def check_collision(self, shape):
        pass

    def _create_rays(self):
        i, j, _ = self.direction
        rays = np.array([self.x + i * 300, self.y + j * 300, 1], ndmin=2)
        return rays

    def draw(self, shift):
        pg = self.game_engine.pg
        x, y = self.x + shift[0], self.y + shift[1]
        rx, ry = self.vision[0, 0] + shift[0], self.vision[0, 1] + shift[1]
        return x, y, rx, ry, pg
