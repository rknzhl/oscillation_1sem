from conditions import Conditions
from wave_animator import WaveAnimator
from wave_solver import WaveSolver

conditions = Conditions(len_x=10, Nx=80, len_y=10, Ny=80, dt=0.025, T=400)
wave_solver = WaveSolver(conditions)
wave_solver.solve_wave_equation()
wave_animator = WaveAnimator(conditions)
wave_animator.animate_wave()