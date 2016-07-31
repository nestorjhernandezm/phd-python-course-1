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


def get_title(initial_conditions, parameters):
    condition_names = ['x_0', 'y_0', 'z_0']
    parameter_names = [r'$\sigma$', r'$\beta$', r'$\rho$']

    title = r'$'
    for name in condition_names:
        value = initial_conditions[condition_names.index(name)]
        title += name + '\ =\ ' + str(value)

        if (name == 'z_0'):
            title += '.\ $'
        else:
            title += ',\ '

    for name in parameter_names:
        value = parameters[parameter_names.index(name)]
        title += name + '$\ =\ $' + '$' + str(value) + '$'

        if (name == r'$\rho$'):
            title += '$.$'
        else:
            title += '$,\ $'

    return title


def create_3d_plot(table, plot_type, parameters):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    if (plot_type == 'plot'):
        ax.plot(table['X'], table['Y'], table['Z'], c='b')

    if (plot_type == 'scatter'):
        color = compute_color(table['X'], table['Y'], table['Z'])
        ax.scatter(table['X'], table['Y'], table['Z'], c=color)

    initial_conditions = (table['X'][0], table['Y'][0], table['Z'][0])
    ax.set_title(get_title(initial_conditions, parameters))
    ax.set_xlabel(r'$X$')
    ax.set_ylabel(r'$Y$')
    ax.set_zlabel(r'$Z$')


def create_2d_plot(table, plot_type, abcissa, ordinate, parameters):
    fig = plt.figure()
    ax = fig.gca()

    if (plot_type == 'plot'):
        ax.plot(table[abcissa], table[ordinate], c='b')

    if (plot_type == 'scatter'):
        color = compute_color(table[abcissa], table[ordinate], 0)
        ax.scatter(table[abcissa], table[ordinate], c=color)

    ax.grid('on')
    initial_conditions = (table['X'][0], table['Y'][0], table['Z'][0])
    ax.set_title(get_title(initial_conditions, parameters), fontsize=12)
    ax.set_xlabel(r'$' + abcissa + '$')
    ax.set_ylabel(r'$' + ordinate + '$')

    plt.tight_layout()
    plt.savefig('test_figure.pdf')


def plot_data(filename):
    df = pd.read_csv(filename)  # Load data into Pandas dataframe
    df_group = df.groupby(by=['Sigma', 'Beta', 'Rho'])

    for keys, group in df_group:
        table = group.pivot_table(['X', 'Y', 'Z'], index=group.index)

#        create_3d_plot(table, 'plot', keys)
#        create_3d_plot(table, 'scatter', keys)
        create_2d_plot(table, 'plot', 'X', 'Y', keys)
#        create_2d_plot(table, 'scatter', 'X', 'Y', keys)
#        create_2d_plot(table, 'plot', 'X', 'Z', keys)
#        create_2d_plot(table, 'scatter', 'X', 'Z', keys)
#        create_2d_plot(table, 'plot', 'Y', 'Z', keys)
#        create_2d_plot(table, 'scatter', 'Y', 'Z', keys)
