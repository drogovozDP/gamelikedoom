import numpy as np
from numpy import sin, cos


def get_move_matrix(x, y):
    return np.array([[1, 0, 0],
                     [0, 1, 0],
                     [x, y, 1]])


def get_rotate_matrix(a, x, y):
    return np.array([[cos(a),              -sin(a),                              0],
                     [sin(a),               cos(a),                              0],
                     [-x * cos(a) - y * sin(a) + x, x * sin(a) - y * cos(a) + y, 1]])
