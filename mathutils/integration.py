import random
import numpy as np


def validate_input(a, b, n):
    if n <= 0:
        raise ValueError("Enter n > 0 please\n")
    if a > b:
        raise ValueError("Enter a < b please\n")


def integrate_rectangles_method(a, b, n, func):
    if a == b:
        return 0
    validate_input(a, b, n)
    h = (b - a) / n
    integral = 0
    for i in range(0, n):
        integral += func(a + i * h)
    return h * integral


def integrate_trapezoid_method(a, b, n, func):
    if a == b:
        return 0
    validate_input(a, b, n)
    h = (b - a) / n
    s = 0
    for i in range(1, n):
        s += func(a + i * h)
    return (h / 2) * (func(a) + func(b) + 2 * s)


def integrate_parabola_method(a, b, n, func):
    if a == b:
        return 0
    validate_input(a, b, n)
    h = (b - a) / (2 * n)
    even_sum = 0
    odd_sum = 0
    for i in range(1, 2 * n):
        if i % 2 == 0:
            even_sum += func(a + i * h)
        else:
            odd_sum += func(a + i * h)

    return (h / 3) * (func(a) + 4 * odd_sum + 2 * even_sum + func(b))


def integrate_cubic_parabola_method(a, b, n, func):
    if a == b:
        return 0
    validate_input(a, b, n)
    h = (b - a) / (3 * n)
    threes_sum = 0
    twos_sum = 0
    for i in range(1, 3 * n):
        if i % 3 == 0:
            twos_sum += func(a + i * h)
        else:
            threes_sum += func(a + i * h)
    return ((3 * h) / 8) * (func(a) + 2 * twos_sum + 3 * threes_sum + func(b))


def integrate_bull_method(a, b, n, func):
    if a == b:
        return 0
    validate_input(a, b, n)
    h = (b - a) / (4 * n)
    thirty_two_sum = 0
    twelve_sum = 0
    fourteen_sum = 0
    for i in range(1, 4 * n):
        if i % 2 != 0:
            thirty_two_sum += func(a + i * h)
        elif i % 2 == 0 and i % 4 != 0:
            twelve_sum += func(a + i * h)
        elif i % 4 == 0:
            fourteen_sum += func(a + i * h)

    return ((2 * h) / 45) * (7 * func(a) + 32 * thirty_two_sum + 14 * fourteen_sum + 12 * twelve_sum + 7 * func(b))


def integrate_monte_carlo(a, b, n, func):
    if a == b:
        return 0
    validate_input(a, b, n)
    u = np.random.rand(n, 1)
    y = func(a + (b - a) * u)
    return ((b - a) / n) * y.sum()


def integrate_gauss(a, b, n, func):
    if a == b:
        return 0
    validate_input(a, b, n)
    xi_arr = [[-0.577350269, 0.577350269], [-0.774596669, 0, 0.774596669],
              [-0.861136312, -0.339981044, 0.339981044, 0.861136312],
              [-0.906179846, -0.538469310, 0, 0.538469310, 0.906179846],
              [-0.932469514, -0.661209386, -0.238619186, 0.238619186, 0.661209386, 0.932469514]]
    c_arr = [[1, 1], [0.555555556, 0.888888889, 0.555555556],
             [0.347854845, 0.652145155, 0.652145155, 0.347854845],
             [0.236926885, 0.478628670, 0.568888889, 0.478628670, 0.236926885],
             [0.171324492, 0.360761573, 0.467913935, 0.467913935, 0.360761573, 0.171324492]]
    integral = 0
    for xi, c in zip(xi_arr[n - 2], c_arr[n - 2]):
        integral += c * func(((a + b) + xi * (b - a)) / 2)
    return (b - a) / 2 * integral
