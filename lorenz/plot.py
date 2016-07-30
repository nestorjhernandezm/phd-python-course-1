"""
This file may contain functionalities for plotting

"""
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd


# ##### PLOTTING SETTINGS ########
font_size = 12

font = {'family': 'sans-serif',
        'weight': 'medium',
        'style': 'normal',
        'size': font_size}
plt.rc('font', **font)
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=font_size)
plt.rc('ytick', labelsize=font_size)


def compute_color(x, y, z):
    distance = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    norm = mpl.colors.Normalize(vmin=min(distance), vmax=max(distance))
    cmap = cm.jet
    mapper = cm.ScalarMappable(norm=norm, cmap=cmap)
    color = []
    for d in distance:
        color.append(mapper.to_rgba(d))
    return color


def plot_data(filename):
    df = pd.read_csv(filename)  # Load data into Pandas dataframe
    df_group = df.groupby(by=['Sigma', 'Beta', 'Rho'])

    for keys, group in df_group:
        table = group.pivot_table(['X', 'Y', 'Z'], index=group.index)
        fig1 = plt.figure()
        fig2 = plt.figure()

        ax1 = fig1.gca(projection='3d')
        ax2 = fig2.gca(projection='3d')

        ax1.plot(table['X'], table['Y'], table['Z'])
        ax1.set_xlabel(r'$X$')
        ax1.set_ylabel(r'$Y$')
        ax1.set_zlabel(r'$Z$')

        color = compute_color(table['X'], table['Y'], table['Z'])
        ax2.scatter(table['X'], table['Y'], table['Z'], c=color)
        ax2.set_xlabel(r'$X$')
        ax2.set_ylabel(r'$Y$')
        ax2.set_zlabel(r'$Z$')
