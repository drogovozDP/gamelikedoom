from engine.game_objects import GameObject
from engine.consts import *
from engine.math_functions import *
import numpy as np


class Entity(GameObject):
    def __init__(self, game_engine, x, y, color):
        super().__init__(game_engine, x, y, color)
        self.size = self.game_engine.graphic.cell_size // 2
        self.velocity = STANDARD_CREATURE_VELOCITY
        self.rotate_angle = ROTATE_ANGLE
        self.direction = np.array([1, 0, 1])
        self.ray = self._create_rays()

    def rotate(self, kfc):
        a = kfc * self.rotate_angle
        R = get_rotate_matrix(a, self.direction[0], self.direction[1])
        self.direction = R @ self.direction
        self.ray = self._create_rays()

    def move(self, dy):
        x, y, _ = dy * self.direction
        M = get_move_matrix(x, y)
        self.x, self.y, _ = np.array([self.x, self.y, 1]) @ M
        for i, ray in enumerate(self.ray):
            self.ray[i] = ray @ M

    def _create_rays(self):
        i, j, _ = self.direction
        rays = np.array([self.x + i * 300, self.y + j * 300, 1], ndmin=2)
        return rays

    def draw(self, shift):
        pg = self.game_engine.pg
        x, y = self.x + shift[0], self.y + shift[1]
        rx, ry = self.ray[0, 0] + shift[0], self.ray[0, 1] + shift[1]
        return x, y, rx, ry, pg
