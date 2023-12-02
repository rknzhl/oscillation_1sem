import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

class WaveAnimator:
    def __init__(self, conditions):
        self.conditions = conditions

    def animate_wave(self):
        print("Начало анимации")
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(self.conditions.x_vec, self.conditions.y_vec)
        surf = ax.plot_surface(X, Y, self.conditions.u[0], cmap='plasma', shade=True, linewidth=0, antialiased=False)

        # Фиксация осей
        ax.set_xlim(self.conditions.x_vec.min(), self.conditions.x_vec.max())
        ax.set_ylim(self.conditions.y_vec.min(), self.conditions.y_vec.max())
        ax.set_zlim(self.conditions.u.min(), self.conditions.u.max())

        def update_plot(frame_number, Z, plot):
            plot[0].remove()
            plot[0] = ax.plot_surface(X, Y, Z[frame_number], cmap='plasma', shade=True, linewidth=0, antialiased=False)

        ani = FuncAnimation(fig, update_plot, frames=self.conditions.T, fargs=(self.conditions.u, [surf]), interval=50)
        ani.save('wave_animation_2D.gif', writer='pillow', fps=30)

        plt.show()
        print("Анимация закончена и сохранена)")

