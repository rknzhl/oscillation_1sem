import numpy as np


class WaveSolver:
    def __init__(self, conditions):
        self.conditions = conditions

    def solve_wave_equation(self):
        for t in range(1, self.conditions.T - 1):
            print(round(t / self.conditions.T * 100), '%')
            for x in range(1, self.conditions.N - 1):
                self.conditions.u[t + 1, x] = self.conditions.c ** 2 * self.conditions.dt ** 2 * (
                    ((self.conditions.u[t, x + 1] - 2 * self.conditions.u[t, x] + self.conditions.u[
                        t, x - 1]) / (self.conditions.dx ** 2))) + 2 * self.conditions.u[t, x] - self.conditions.u[
                                                  t - 1, x]
