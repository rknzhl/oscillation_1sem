import numpy as np


class Conditions:
    def __init__(self, len_x, N, dt, T):
        self.len_x = len
        self.N = N
        self.dt = dt
        self.T = T

        self.x_vec = np.linspace(0, len_x, num=N)
        self.dx = self.x_vec[2] - self.x_vec[1]

        self.c = 1

        self.u = np.zeros((self.T, len(self.x_vec)))
        self.u[0, 1] = 10
