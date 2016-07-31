import scipy as sp


def compute_states(x0, y0, z0, sigma, beta, rho, N, t_delta):
    """
    This function computes the states x, y and z of the attractor.

    Inputs:
    x0, y0, z0: Coordinates of the initial conditions
    sigma, beta, rho: Attractor parameters
    N, t_delta: Total number of coordinate points and step size
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
