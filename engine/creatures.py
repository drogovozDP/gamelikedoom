from engine.game_objects import GameObject
from engine.consts import *
from engine.math_functions import *
from engine.raycasting import Ray
import numpy as np


class Entity(GameObject):
    def __init__(self, game_engine, x, y, color):
        super().__init__(game_engine, x, y, color)
        self.radius = self.game_engine.graphic.cell_size // 3
        self.shape = create_circle_shape(x, y, self.radius, 10)
        self.velocity = STANDARD_CREATURE_VELOCITY
        self.rotate_velocity = ROTATE_VELOCITY
        self.direction = np.array([1, 0, 1])
        self.vision = Ray(game_engine, x, y, RAY, 200, self.direction)

    def rotate(self, kfc):
        a = kfc * ROTATE_VELOCITY
        R = get_rotate_matrix(a, self.direction[0], self.direction[1])
        self.direction = R @ self.direction
        self.vision.rotate(R)
        # self.vision = self._create_rays()

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
        self.vision.move(M)
        # for i, ray in enumerate(self.vision):  # move a rays
        #     self.vision[i] = ray @ M

    def check_collision(self, shape):
        pass

    # def _create_rays(self):
    #     i, j, _ = self.direction
    #     rays = np.array([self.x + i * 300, self.y + j * 300, 1], ndmin=2)
    #     return rays

    def look_around(self):
        objects, env_to_draw = self.vision.collision()
        if objects is not None:
            objects.test()

    def draw(self, shift):
        pg = self.game_engine.pg
        x, y = self.x + shift[0], self.y + shift[1]
        # rx, ry = self.vision[0, 0] + shift[0], self.vision[0, 1] + shift[1]
        rx, ry, _ = self.vision.length * self.vision.direction
        rx, ry = rx + shift[0] + self.vision.x, ry + shift[1] + self.vision.y
        return x, y, rx, ry, pg
