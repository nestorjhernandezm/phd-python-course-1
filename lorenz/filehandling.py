"""
This file can contain functionalities for saving/loading data

"""
import scipy as sp


def save_data(filename, data):
    """
    Save the data as rows in a CSV file. The format of the file is:

    Sigma   Beta  Rho   N    T_delta   X     Y     Z
      s0     b0   r0    n0   t_d0      x0    y0    z0
      s0     b0   r0    n0   t_d0      x1    y1    z1
      s0     b0   r0    n0   t_d0      x2    y2    z2
      ..................................................
      s0     b0   r0    n0   t_d0      xn0-1 yn0-1 zn0-1
      --------------------------------------------------
      s1     b1   r1    n1   t_d1      x0    y0    z0
      s1     b1   r1    n1   t_d1      x1    y1    z1
      s1     b1   r1    n1   t_d1      x2    y2    z2
      ..................................................
      s1     b1   r1    n1   t_d1      xn1-1 yn1-1 zn1-1
      --------------------------------------------------
      ..................................................
      ..................................................
      ..................................................

    Where first, the attractor states are stored as columns for
    a first fixed set of parameters, later a second, third and so on as
    required.

    Input:
    filename: String for the name of the file to store the data
    data: Scipy 2D array with the indicated values acalculated previously.
    """
    f = open(filename, 'w')
    f.write('Sigma,Beta,Rho,N,T_delta,X,Y,Z\n')
    sp.savetxt(f, data, delimiter=',')
    f.close()
