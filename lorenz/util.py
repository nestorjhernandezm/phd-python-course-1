"""
This file may contain utility functionalities to the extend you will need it

"""
import scipy as sp
import solver as sv


def generate_data_case(sigma, beta, rho, N, t_delta, x, y, z):
    """
    Generate output data for a given case for later processing. The output
    is a 2D array containing the all the states and the conditions
    used to generate them as columns for the given case. This will simplify
    the processing and plotting at a later stage.

    Input:
    sigma: Integer for the sigma attractor parameter
    beta: Float64 for the beta attractor parameter
    rho: Integer for the rho attractor parameter
    N: Integer for the total number of steps of the solver
    t_delta: Float64 for the step size of the solver
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


def generate_dataset(x0, y0, z0, N, t_delta, cases):
    """
    Generate full dataset for all the sigma, beta, rho parameters
    considered in the 'cases' list. Each member of list is a tuple
    of fixed sigma, beta and rho values of the attractor.

    Inputs:
    x0: Integer for the initial condition for the x-position
    y0: Float64 for the initial condition for the y-position
    z0: Integer for the initial condition for the z-position
    N: Integer for the total number of steps of the solver
    t_delta: Float64 for the step size of the solver
    cases: List of tuple, where each tuple is of the type (sigma, beta, rho)
    """
    dataset = sp.zeros([1, 8])  # Just to create the first concatenate

    for sigma, beta, rho in cases:
        x, y, z = sv.compute_states(x0, y0, z0, sigma, beta, rho, N, t_delta)

        # Give data an array format
        data = generate_data_case(sigma, beta, rho, N, t_delta, x, y, z)
        dataset = sp.concatenate((dataset, data), axis=0)

    dataset = sp.delete(dataset, (0), axis=0)  # Remove the first row of zeros

    return dataset
