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
import filehandling as fh
import scipy as sp

import pandas as pd

x0 = 1
y0 = 1
z0 = 1

sigma = 10
beta = 8./3
rho = 6
N = 200
t_delta = 0.01

x, y, z = sv.calculate_states(x0, y0, z0, sigma, beta, rho, N, t_delta)

data = fh.generate_data(sigma, beta, rho, N, t_delta, x, y, z)
sp.savetxt('data.csv', data, delimiter=',')

df = pd.read_csv('data.csv')
