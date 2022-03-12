import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def function(x, y):
    return np.sqrt(x*x+y*y)+3*np.cos(np.sqrt(x*x+y*y))**2+5


def analytical_derivative_x(x, y):
    return -(6*x*np.sin(np.sqrt(x**2+y**2))*np.cos(np.sqrt(x**2+y**2)))/(np.sqrt(x**2+y**2)) + x/np.sqrt(x**2+y**2)


def analytical_derivative_y(x, y):
    return -(6*y*np.sin(np.sqrt(x**2+y**2))*np.cos(np.sqrt(x**2+y**2)))/(np.sqrt(x**2+y**2)) + y/np.sqrt(x**2+y**2)


def numerical_derivative_x(x, y, step):
    return (function(x + step, y) - function(x - step, y)) / (2 * step)


def numerical_derivative_y(x, y, step):
    return (function(x, y + step) - function(x, y - step)) / (2 * step)


def draw_function():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')

    xval = np.linspace(-5.0, 5.0, 100)
    yval = np.linspace(-5.0, 5.0, 100)
    x, y = np.meshgrid(xval, yval)

    f = function(x, y)

    ax.set(xlabel='x', ylabel='y', zlabel='f', title='function = sqrt(x*x+y*y)+3*cos(sqrt(x*x+y*y))^2+5')
    ax.plot_surface(x, y, f, rstride=1, cstride=1, cmap=cm.plasma)
    plt.show()


if __name__ == '__main__':
    x = 2.5
    y = 5.0
    step = 1e-5

    draw_function()

    print("\nfunction value at x = {0} y = {1} is {2}\n".format(x, y, function(x, y)))
    print("analytical partial derivative Dx value at x = {0} y = {1} is {2}".format(x, y, analytical_derivative_x(x, y)))
    print("numerical partial derivative Dx value at x = {0} y = {1} with step = {2} is {3}\n".format(x, y, step, numerical_derivative_x(x, y, step)))
    print("analytical partial derivative Dy value at x = {0} y = {1} is {2}".format(x, y, analytical_derivative_y(x, y)))
    print("numerical partial derivative Dy value at x = {0} y = {1} with step = {2} is {3}\n".format(x, y, step, numerical_derivative_y(x, y, step)))
