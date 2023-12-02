import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class WaveAnimator1D:
    def __init__(self, conditions):
        self.conditions = conditions

    def animate_wave(self):
        print("Начало анимации")
        fig, ax = plt.subplots()
        x = self.conditions.x_vec
        line, = ax.plot(x, self.conditions.u[0], color='blue')

        ax.set_xlim(x.min(), x.max())
        ax.set_ylim(-40, 40)

        def update_plot(frame_number, data, line):
            line.set_ydata(data[frame_number])

        ani = FuncAnimation(fig, update_plot, frames=self.conditions.T, fargs=(self.conditions.u, line), interval=50,
                            blit=False)
        ani.save('wave_animation_1D.gif', writer='pillow', fps=30)

        plt.show()
        print("Анимация закончена и сохранена)")
