"""
This file may contain a convenient interface/function for

1: computing a trajectory using an ODE solver from solver.py
2: save data to file
3: plot data

and possible another function that

2: load data from file  --------------> This is made in each case.py
3: plot data            --------------> This is made in each case.py

"""
import util as ut
import filehandling as fh

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

cases = [case1, case2, case3, case4, case5]
dataset = ut.generate_dataset(x0, y0, z0, N, t_delta, cases)

filename = 'data.csv'
fh.save_data(filename, dataset)
