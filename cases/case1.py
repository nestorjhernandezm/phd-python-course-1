"""
This file could contain the necessary calls to make plots etc for
case 1

"""
import os
import pandas as pd
import plot as pl

if (os.path.isfile('../lorenz/data.csv')):
    df = pd.read_csv('../lorenz/data.csv')
    df_case1 = df[(df['Sigma'] == 10) & (df['Beta'] == 10) &
                  (df['Rho'] == 6)]
    pl.plot_data(df_case1)
else:
    print "foo"
