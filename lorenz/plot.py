"""
This file may contain functionalities for plotting

"""
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt


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
    """
    Compute the color array in the jet colormap, for the distance of
    the points with coordinate arrays (x, y, z) and the origin. The returned
    array is used with the scatter plot.

    NOTE: The simple 'plot' command was not able to take this as an input.

    Inputs:
    x: Scipy array for the x-positions
    y: Scipy array for the y-positions
    z: Scipy array for the z-positions
    """
    distance = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    norm = mpl.colors.Normalize(vmin=min(distance), vmax=max(distance))
    cmap = cm.jet
    mapper = cm.ScalarMappable(norm=norm, cmap=cmap)
    color = []
    for d in distance:
        color.append(mapper.to_rgba(d))
    return color


title_value = {'10.0': r'10',
               '2.66666666667': r'\frac{8}{3}',
               '6.0': r'6'
               }


def get_title(initial_conditions, parameters):
    """
    Generate plot title in LaTeX format from the initial conditions
    (x0, y0 and z0) and the atracttor parameters.

    Inputs:
    initial_conditions: Tuple for (x0,y0,z0)
    parameters: Tuple for (sigma, beta, rho)
    """
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
        title += name + '$\ =\ $' + '$' + title_value[str(value)] + '$'

        if (name == r'$\rho$'):
            title += '$.$'
        else:
            title += '$,\ $'

    return title


def get_plot_filename(initial_conditions, parameters):
    """
    Generate plot PDF filensame in simple text format from the
    initial conditions (x0, y0 and z0) and the atracttor parameters.

    Inputs:
    initial_conditions: Tuple for (x0,y0,z0)
    parameters: Tuple for (sigma, beta, rho)
    """
    condition_names = ['x0', 'y0', 'z0']
    parameter_names = ['sigma', 'beta', 'rho']
    names = condition_names + parameter_names
    full_parameters = initial_conditions + parameters

    plot_filename = ''
    for name in names:
        value = full_parameters[names.index(name)]
        plot_filename += name + '_' + str(value)

        if (name != 'rho'):
            plot_filename += '_'

    return plot_filename


def create_3d_plot(table, plot_type, parameters):
    """
    Create and save full 3D plot from the attractor states
    and given parameters. If 'scatter' is selected as plot_type,
    a point is colored according its Euclidean distance from the origin.

    Inputs:
    table: Pandas dataframe with the states for fixed parameters
    plot_type: String for seleting the plot type
    parameters: Tuple for (sigma, beta, rho)
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    if (plot_type == 'plot'):
        ax.plot(table['X'], table['Y'], table['Z'], c='b')

    if (plot_type == 'scatter'):
        color = compute_color(table['X'], table['Y'], table['Z'])
        ax.scatter(table['X'], table['Y'], table['Z'], c=color)

    initial_conditions = (table['X'][0], table['Y'][0], table['Z'][0])
    ax.set_title(get_title(initial_conditions, parameters), fontsize=10)
    ax.set_xlabel(r'$X$')
    ax.set_ylabel(r'$Y$')
    ax.set_zlabel(r'$Z$')

    name = get_plot_filename(initial_conditions, parameters)
    plt.savefig(name + '_' + plot_type + '_full_3D.pdf')


def create_2d_plot(table, plot_type, abcissa, ordinate, parameters):
    """
    Create and save a 2D abcissa-ordinate plot from the attractor state
    and given parameters. If 'scatter' is selected as plot_type,
    a point is colored according its Euclidean distance from the origin.

    Inputs:
    table: Pandas dataframe with the states for fixed parameters
    plot_type: String for seleting the plot type
    abcissa: String for the selected abcissa axis
    ordinate: String for the selected ordinate axis
    parameters: Tuple for (sigma, beta, rho)
    """
    fig = plt.figure()
    ax = fig.gca()

    if (plot_type == 'plot'):
        ax.plot(table[abcissa], table[ordinate], c='b')

    if (plot_type == 'scatter'):
        color = compute_color(table[abcissa], table[ordinate], 0)
        ax.scatter(table[abcissa], table[ordinate], c=color)

    ax.grid('on')
    initial_conditions = (table['X'][0], table['Y'][0], table['Z'][0])
    ax.set_title(get_title(initial_conditions, parameters), fontsize=10)
    ax.set_xlabel(r'$' + abcissa + '$')
    ax.set_ylabel(r'$' + ordinate + '$')

    name = get_plot_filename(initial_conditions, parameters)
    plt.savefig(name + '_' + plot_type + '_2D_' + abcissa + ordinate +
                '_plane.pdf')


def plot_data(df):
    """
    Create and save a set of 3D and 2D abcissa-ordinate plots from the
    attractor state and given parameters stored in the dataframe 'df'.
    The plots are stored locally in the 'lorenz' folder and
    are separated for a fixed set of the attractor parameters.

    Inputs:
    df: Pandas datafrane with the dataset
    """
    df_group = df.groupby(by=['Sigma', 'Beta', 'Rho'])

    for keys, group in df_group:
        table = group.pivot_table(['X', 'Y', 'Z'], index=group.index)

        create_3d_plot(table, 'plot', keys)
        create_3d_plot(table, 'scatter', keys)
        create_2d_plot(table, 'plot', 'X', 'Y', keys)
        create_2d_plot(table, 'scatter', 'X', 'Y', keys)
        create_2d_plot(table, 'plot', 'X', 'Z', keys)
        create_2d_plot(table, 'scatter', 'X', 'Z', keys)
        create_2d_plot(table, 'plot', 'Y', 'Z', keys)
        create_2d_plot(table, 'scatter', 'Y', 'Z', keys)
