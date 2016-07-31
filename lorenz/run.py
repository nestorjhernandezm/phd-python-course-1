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
import scipy as sp

# Initial Condition
x0 = 0.01
y0 = 0
z0 = 0

# Solver parameters
N = 5000
t_delta = 0.01

# Attractor parameters (sigma, beta, rho)
case1 = (10, 8./3, 6)
case2 = (10, 8./3, 16)
case3 = (10, 8./3, 28)
case4 = (14, 8./3, 28)
case5 = (14, 13./3, 28)

dataset = sp.zeros([1, 8])

for sigma, beta, rho in [case1, case2, case3, case4, case5]:
    x, y, z = sv.compute_states(x0, y0, z0, sigma, beta, rho, N, t_delta)

    # Give data an array format
    data = ut.generate_data(sigma, beta, rho, N, t_delta, x, y, z)
    dataset = sp.concatenate((dataset, data), axis=0)

# Remove the first row of zeros
dataset = sp.delete(dataset, (0), axis=0)

#filename = 'data.csv'
#fh.save_data(filename, data)
#
## Plot data file
#pl.plot_data(filename)
