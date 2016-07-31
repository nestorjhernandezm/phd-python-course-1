"""
This file may contain utility functionalities to the extend you will need it

"""
import scipy as sp


def generate_data(sigma, beta, rho, N, t_delta, x, y, z):
    """
    Generate output data for later processing. The output
    is a 2D array containing the all the states and the conditions
    used to generate them as columns. This will simplify the processing
    and plotting at a later stage.

    Input:
    sigma: Sigma parameter of the attractor (integer)
    beta: Beta parameter of the attractor (default float64 for decimal numbers)
    rho: Rho parameter of the attractor (integer)
    N: Total number of steps of the algorithm (integer)
    t_delta: step of the solver (default float64 for decimal numbers)
    x: Scipy array for the x-positions
    y: Scipy array for the y-positions
    z: Scipy array for the z-positions
    """
    S = sigma * sp.ones([N, 1])
    B = beta * sp.ones([N, 1])
    R = rho * sp.ones([N, 1])
    Na = N * sp.ones([N, 1])
    T = t_delta * sp.ones([N, 1])

    data = sp.column_stack((S, B, R, Na, T, x, y, z))
    return data
