import numpy as np
import matplotlib.pyplot as plt
from trainings.wk_utils import utils as wk_utils


def plot_function(func, start=-10.0, end=10.0, step=0.1):
    x = np.arange(start, end, step)
    y = [func(i) for i in x]
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x')
    # naming the y axis
    plt.ylabel('y')

    # giving a title to my graph
    plt.title('f')

    # function to show the plot
    plt.show()


def plot_points_on_plt(plt_ref, points, label : str):

    x, y = wk_utils.decompose_to_lists(points)

    plt_ref.scatter(x, y, label = label)


    # plt.plot(x, y, label="line 1")
    # plt.plot(y, x, label="line 2")
    # plt.plot(x, np.sin(x), label="curve 1")
    # plt.plot(x, np.cos(x), label="curve 2")
    # plt.legend()
    # plt.show()