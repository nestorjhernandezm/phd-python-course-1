"""
This file may contain functionalities for plotting

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd


# ##### PLOTTING SETTINGS ########
font_size = 14

font = {'family': 'sans-serif',
        'weight': 'medium',
        'style': 'normal',
        'size': font_size}
plt.rc('font', **font)
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=font_size)
plt.rc('ytick', labelsize=font_size)


def plot_data(filename):
    df = pd.read_csv(filename)  # Load data into Pandas dataframe
    df_group = df.groupby(by=['Sigma', 'Beta', 'Rho'])

    for keys, group in df_group:
        table = group.pivot_table(['X', 'Y', 'Z'], index=group.index)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot(table['X'], table['Y'], table['Z'], color='jet')
        ax.set_xlabel(r'$X$')
        ax.set_ylabel(r'$Y$')
        ax.set_zlabel(r'$Z$')
