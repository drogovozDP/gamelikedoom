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


def create_circle_shape(x0, y0, r, n):
    x = lambda t: r * cos(t) + x0
    y = lambda t: r * sin(t) + y0
    return np.array([np.array([x(t), y(t), 1]) for t in np.linspace(0, 2 * np.pi, n)])
