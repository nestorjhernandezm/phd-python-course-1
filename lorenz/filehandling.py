"""
This file can contain functionalities for saving/loading data

"""

import scipy as sp


def generate_data(sigma, beta, rho, N, t_delta, x, y, z):
    """
    Generate output data for later processing. The output
    is an array containing the all the states and the conditions
    used to generate them. This will simplify the processing at
    a later stage.
    """
    S = sigma * sp.ones([N, 1])
    B = beta * sp.ones([N, 1])
    R = rho * sp.ones([N, 1])
    Na = N * sp.ones([N, 1])
    T = t_delta * sp.ones([N, 1])

    data = sp.column_stack((S, B, R, Na, T, x, y, z))
    return data
