import scipy as sp


def solver(x0, y0, z0, sigma, beta, rho, N, t_delta):
    """
    The ODE Solver for the project: This function calculates
    the vectors x, y and z for the trajectories of the attractor.

    Inputs:
    x0, y0, z0: Coordinates of the initial condition
    sigma, beta, rho: Attractor parameters
    N, t_delta: Total number of trajectory points and solver step
    """
    x = sp.zeros([N, 1])
    y = sp.zeros([N, 1])
    z = sp.zeros([N, 1])

    x[0] = x0
    y[0] = y0
    z[0] = z0

    for n in range(N - 1):
        x[n + 1] = x[n] + t_delta * (sigma * (y[n] - x[n]))
        y[n + 1] = y[n] + t_delta * (x[n] * (rho - z[n]) - y[n])
        z[n + 1] = z[n] + t_delta * (x[n] * y[n] - (beta * z[n]))

    return x, y, z


x, y, z = solver(1, 1, 1, 10, 8./3, 6, 1000, 0.01)
