import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from cubic_spline_3d import *


def calculate_3d_spline_interpolation(x, y, z, num=100):
    cubic_spline_3d = CubicSpline3D(x, y, z)
    params = np.linspace(cubic_spline_3d.params[0], cubic_spline_3d.params[-1], num + 1)

    result_x, result_y, result_z = [], [], []
    for param in params:
        point_x, point_y, point_z = cubic_spline_3d.point(param)
        result_x.append(point_x)
        result_y.append(point_y)
        result_z.append(point_z)

    return result_x, result_y, result_z


if __name__ == '__main__':
    x_points = [1, 2, 3, 4, 5]
    y_points = [1, 10, 10, -8, 0]
    z_points = [-1, 4, 5, 5, -6]

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')

    points = ax.plot(x_points, y_points, z_points, "x")

    x_curve_points, y_curve_points, z_curve_points = calculate_3d_spline_interpolation(x_points, y_points, z_points, num=500)
    curve = ax.plot(x_curve_points, y_curve_points, z_curve_points, "-g", label="spline")

    fig.canvas.draw()
    plt.show()
