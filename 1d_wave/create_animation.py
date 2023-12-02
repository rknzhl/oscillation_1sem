from conditions import Conditions
from wave_animator import WaveAnimator1D
from wave_solver import WaveSolver

conditions = Conditions(len_x=10, N=200, dt=0.025, T=800)
wave_solver = WaveSolver(conditions)
wave_solver.solve_wave_equation()
wave_animator = WaveAnimator1D(conditions)
wave_animator.animate_wave()