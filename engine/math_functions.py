import numpy as np
from numpy import sin, cos


def get_rotate_matrix(a):
    return np.array([[cos(a), -sin(a)],
                     [sin(a),  cos(a)]])


def get_move_matrix(x, y):
    return np.array([[x, 1],
                     [1, y]])
