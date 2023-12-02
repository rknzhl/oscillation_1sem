import numpy as np

class Conditions:
    def __init__(self, len_x, Nx, len_y, Ny, dt, T):
        self.len_x = len_x
        self.Nx = Nx
        self.len_y = len_y
        self.Ny = Ny
        self.dt = dt
        self.T = T

        self.x_vec = np.linspace(0, len_x, Nx)
        self.dx = self.x_vec[2] - self.x_vec[1]

        self.y_vec = np.linspace(0, len_y, Ny)
        self.dy = self.y_vec[2] - self.y_vec[1]

        self.c = 1

        self.u = np.zeros([T, len(self.x_vec), len(self.y_vec)])
        self.u[0, Nx // 2, Ny // 2] = 10

        for i in range(0, Nx):
            self.u[0, i, Ny // 2] = 10