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
        self.ray = np.array([x, y + 300], ndmin=2)

    def rotate(self, kfc):
        R = get_rotate_matrix(kfc * self.rotate_angle)
        M = get_move_matrix(self.x, self.y)
        for i, ray in enumerate(self.ray):
            self.ray[i] = ray @ R
        self.x, self.y = np.array([self.x, self.y]) @ R

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.ray[0, 0] += dx
        self.ray[1, 0] += dy

    def draw(self, shift):
        pg = self.game_engine.pg
        x, y = self.x + shift[0], self.y + shift[1]
        rx, ry = self.ray[0, 0] + shift[0], self.ray[0, 1] + shift[1]
        return x, y, rx, ry, pg
