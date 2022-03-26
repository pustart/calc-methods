import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import matplotlib as mpl

from mathutils import *


def sample_function_1(x):
    return 5 * (np.sin(x) - 3) ** 2 + 1


def sample_function_2(x):
    return (x + 3) ** 2


def sample_function_3(x):
    return x ** 4 + 8 * x ** 3 - 6 * x ** 2 + 12 * x


def analyzing_h(func, integrating_method, a, b, n):
    original = integrating_method(a, b, 10000, func)
    data = []
    for i in n:
        data.append(abs(original - integrating_method(a, b, i, func)))
    return data


def show_analytics(func, a, b, n, step):
    x = np.arange(1, n, step)
    h = (b - a) / x

    mpl.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(h, analyzing_h(func, integration.integrate_rectangles_method, a, b, x), c="g", label="rec")
    ax.plot(h, analyzing_h(func, integration.integrate_trapezoid_method, a, b, x), c="m", label="trap")
    ax.plot(h, analyzing_h(func, integration.integrate_parabola_method, a, b, x), c="b", label="parabola")
    ax.plot(h, analyzing_h(func, integration.integrate_cubic_parabola_method, a, b, x), c="y", label="cub_porab")
    ax.plot(h, analyzing_h(func, integration.integrate_bull_method, a, b, x), c="r", label="bull")
    ax.set(xlabel='x', ylabel='f', title='part 2, analyzing')

    plt.yscale('log')
    ax.grid()
    ax.legend()

    plt.show()


def show_integration(a, b, n, function):
    print("==========================\nCustom integration: ")
    print("rectangles: {}".format(integration.integrate_rectangles_method(a, b, n, function)))
    print("Monte Carlo: {}".format(integration.integrate_monte_carlo(a, b, n, function)))
    print("trapezoid: {}".format(integration.integrate_trapezoid_method(a, b, n, function)))
    print("parabola: {}".format(integration.integrate_parabola_method(a, b, n, function)))
    print("cubic parabola: {}".format(integration.integrate_cubic_parabola_method(a, b, n, function)))
    print("bull: {}".format(integration.integrate_bull_method(a, b, n, function)))
    print("==========================\nLibrary integration: ")
    print("rectangles: {}".format(integrate.quad(function, a, b)[0]))
    print("==========================\nGauss integration: ")
    for point in range(2, 7):
        print("with {0} points: {1}".format(point, integration.integrate_gauss(a, b, point, function)))


if __name__ == '__main__':
    a = 0
    b = 2
    n = 1000
    function = sample_function_3
    show_integration(a, b, n, function)
    step = 5
    show_analytics(function, a, b, n, step)
