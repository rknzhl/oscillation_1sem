import numpy as np

class WaveSolver:
    def __init__(self, conditions):
        self.conditions = conditions

    def solve_wave_equation(self):
        for t in range(1, self.conditions.T - 1):
            print(round(t/self.conditions.T*100), '%')
            for x in range(1, self.conditions.Nx-1):
                for y in range(1, self.conditions.Ny-1):
                    #if (t < 10): #возбуждение в центре плоскости
                    #   self.conditions.u[t, self.conditions.Nx // 4, self.conditions.Ny // 2] = np.sin(t / 1)

                    self.conditions.u[t+1, x, y] = self.conditions.c**2 * self.conditions.dt**2 * (
                        ((self.conditions.u[t, x+1, y] - 2*self.conditions.u[t, x, y] + self.conditions.u[t, x-1, y])/(self.conditions.dx**2)) +
                        ((self.conditions.u[t, x, y+1] - 2*self.conditions.u[t, x, y] + self.conditions.u[t, x, y-1])/(self.conditions.dy**2))
                    ) + 2*self.conditions.u[t, x, y] - self.conditions.u[t-1, x, y]
