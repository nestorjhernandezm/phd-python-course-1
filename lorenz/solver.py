import scipy as sp


def compute_states(x0, y0, z0, sigma, beta, rho, N, t_delta):
    """
    This function computes the states x, y and z of the attractor using
    an approximation based on the Euler method as an ODE solver.

    Inputs:
    x0: Integer for the initial condition for the x-position
    y0: Float64 for the initial condition for the y-position
    z0: Integer for the initial condition for the z-position
    sigma: Integer for the sigma attractor parameter
    beta: Float64 for the beta attractor parameter
    rho: Integer for the rho attractor parameter
    N: Integer for the total number of steps of the solver
    t_delta: Float64 for the step size of the solver
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
