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
import csv


x0 = 1
y0 = 1
z0 = 1
sigma = 10
beta = 8./3
rho = 6
N = 200
t_delta = 0.01

x, y, z = sv.calculate_states(x0, y0, z0, sigma, beta, rho, N, t_delta)


resultFile = open("./test.csv",'wb')
wr = csv.writer(resultFile)
wr.writerows(x)
resultFile.close()