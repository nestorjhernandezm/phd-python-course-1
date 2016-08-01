# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:26:18 2016

@author: nestor
"""
import os
import shutil
import glob
import pandas as pd
import sys
sys.path.append('../lorenz')
import plot as pl
import util as ut
import filehandling as fh

# According to the called script, get the relevant parameter set
file_parameters = {'1': (10, 2.6666666666666661, 8./3, 6),
                   '2': (10, 2.6666666666666661, 8./3, 16),
                   '3': (10, 2.6666666666666661, 8./3, 28),
                   '4': (14, 2.6666666666666661, 8./3, 28),
                   '5': (14, 4.3333333333333333, 13./3, 28)
                   }

testcase = sys.argv[1]

sigma = file_parameters[testcase][0]
beta_df = file_parameters[testcase][1]
beta = file_parameters[testcase][2]
rho = file_parameters[testcase][3]

filename = 'data_case' + testcase + '.csv'

if (os.path.isfile('../lorenz/data.csv')):
    df = pd.read_csv('../lorenz/data.csv')

    # Get only relevant slice of the full dataset
    df_case = df[(df['Sigma'] == sigma) & (df['Beta'] == beta_df) &
                 (df['Rho'] == rho)]
    pl.plot_data(df_case)

else:  # If data file is not there, calculate only the relevant dataset

    # Initial Condition
    x0 = 0.01
    y0 = 0
    z0 = 0

    # Solver parameters
    N = 5000
    t_delta = 0.01
    case = (sigma, beta, rho)
    dataset = ut.generate_dataset(x0, y0, z0, N, t_delta, [case])
    fh.save_data(filename, dataset)

    # Load and plot data from new file
    df = pd.read_csv(filename)
    pl.plot_data(df)

# Move the data and all pdf files to folder
data_folder = './case' + testcase + '_files'
os.mkdir(data_folder)
shutil.move('./' + filename, data_folder)

for f in glob.glob("./*.pdf"):
    shutil.move(f, data_folder)
