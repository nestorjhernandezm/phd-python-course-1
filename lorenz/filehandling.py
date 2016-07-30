"""
This file can contain functionalities for saving/loading data

"""
import scipy as sp


def save_data(filename, data):
    f = open(filename, 'w')
    f.write('Sigma,Beta,Rho,N,T_delta,X,Y,Z\n')
    sp.savetxt(f, data, delimiter=',')
    f.close()
