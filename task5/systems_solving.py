import numpy as np

ACCURACY = 1e-10


def __is_system_suitable(a, b):
    for row in range(0, len(a)):
        if len(a[row]) != len(b):
            print('Wrong dimensions')
            return False

    for row in range(0, len(a)):
        if a[row][row] == 0:
            print('There are zero equal elements on main diagonal')
            return False
    return True


def solve_jacobi(a, b, iter_limit):
    if not __is_system_suitable(a, b):
        raise ValueError('Unsuitable system')

    x = np.zeros_like(b)

    for it_count in range(iter_limit):
        newest_x = x.copy()

        for i in range(len(a[0])):
            a_sum = 0.0

            for j in range(len(a[0])):
                if i != j:
                    a_sum += a[i][j] * x[j]
            newest_x[i] = (b[i] - a_sum) / a[i][i]

        if np.allclose(x, newest_x, atol=ACCURACY):
            break

        x = newest_x
    return x


def solve_seidel(a, b, iter_limit):
    if not __is_system_suitable(a, b):
        raise ValueError('Unsuitable system')

    x = np.zeros_like(b)
    iterations_arr = np.zeros_like(b)

    for counter in range(iter_limit):
        for i in range(len(a[0])):
            a_sum = 0.0

            for j in range(len(a[0])):
                if i != j:
                    a_sum += a[i][j] * x[j]
            x[i] = (b[i] - a_sum) / a[i][i]

        iterations_arr = np.vstack((iterations_arr, x.copy()))

        if np.allclose(iterations_arr[counter], iterations_arr[counter + 1], atol=ACCURACY):
            break
    return x
