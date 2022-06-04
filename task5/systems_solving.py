import numpy as np

ACCURACY = 1e-10


def is_system_suitable(a, b):
    for row in range(0, len(a)):
        if len(a[row]) != len(b):
            print('Wrong dimensions')
            return False

    for row in range(len(a)):
        if a[row][row] != max(a[row]) or a[row][row] == 0:
            print('Diagonal elements dont surpass')
            return False

    return True


def solve_jacobi(a, b, iter_bound):
    if not is_system_suitable(a, b):
        raise ValueError('Unsuitable system')

    x = np.zeros(len(b))

    for it_count in range(iter_bound):
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


def solve_seidel(a, b, iter_bound):
    if not is_system_suitable(a, b):
        raise ValueError('Unsuitable system')

    x = np.zeros(len(b))
    iterations_arr = np.zeros(len(b))

    for counter in range(iter_bound):
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
