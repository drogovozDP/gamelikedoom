from engine.game_objects import GameObject
from engine.consts import *
from engine.math_functions import *
import numpy as np


class RayCasting:
    def __init__(self, game_engine, x, y, direction, ray_count, length):
        self.rays = self._create_rays(game_engine, x, y, length, direction, ray_count // 2)

    def _create_rays(self, game_engine, x, y, length, direction, ray_count):
        view_range = 1 / (ray_count * 2)
        return [
            Ray(game_engine, x, y, RAY, length,
                get_rotate_matrix(i * view_range, x, y) @ direction, np.cos(i * view_range))
            for i in range(-ray_count, ray_count, 1)
        ]

    def rotate(self, R):
        [ray.rotate(R) for ray in self.rays]

    def move(self, M):
        [ray.move(M) for ray in self.rays]

    def collision(self):
        return np.array([ray.collision() for ray in self.rays])


class Ray(GameObject):
    def __init__(self, game_engine, x, y, clr, length, direction, cos):
        super().__init__(game_engine, x, y, COLOR[clr])
        self.length = length
        self.direction = direction
        self.cos = cos

    def collision(self, *args):
        for length in np.linspace(0, self.length, RAY_RATE):
            obj = self.check_collision(length)
            if obj is not None:
                return {RAY_OBJ: obj, RAY_LEN: length, RAY_COS: self.cos}
        return {RAY_OBJ: None, RAY_LEN: self.length, RAY_COS: self.cos}

    def check_collision(self, length):
        dx, dy, _ = length * self.direction
        M = get_move_matrix(dx, dy)
        x, y, _ = np.array([self.x, self.y, 1]) @ M
        for obj in self.game_engine.environment:
            if obj.check_collision([[x, y, 1]]):
                return obj
        return None

    def rotate(self, R):
        self.direction = R @ self.direction

    def move(self, M):
        self.x, self.y, _ = np.array([self.x, self.y, 1]) @ M
