"""
This file may contain a convenient interface/function for

1: computing a trajectory using an ODE solver from solver.py
2: save data to file
3: plot data

and possible another function that

2: load data from file
3: plot data

"""
import solver as sv
import util as ut
import filehandling as fh
import plot as pl

# Initial Condition
x0 = 0.01
y0 = 0
z0 = 0

# Attractor parameters
sigma = 10
beta = 8./3
rho = 28
N = 5000
t_delta = 0.01

# States computation
x, y, z = sv.compute_states(x0, y0, z0, sigma, beta, rho, N, t_delta)

# Give data an array format and store in a local data file
data = ut.generate_data(sigma, beta, rho, N, t_delta, x, y, z)
filename = 'data.csv'
fh.save_data(filename, data)

# Plot data file
pl.plot_data(filename)
