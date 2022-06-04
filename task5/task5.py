import matplotlib.pyplot as plt
import numpy as np
from systems_solving import solve_jacobi
from systems_solving import solve_seidel


def draw_function(a, b):
    jacobian, seidel = [], []
    absolute = np.linalg.solve(a, b)
    x = np.arange(1, 100, 1)

    for n in x:
        dx1, dx2 = 0.0, 0.0
        jacobi_result, seidel_result = solve_jacobi(a, b, n), solve_seidel(a, b, n)

        for p in range(len(a[0])):
            dx1 += abs(jacobi_result[p] - absolute[p]) ** 2
            dx2 += abs(seidel_result[p] - absolute[p]) ** 2

        dx1 = np.sqrt(dx1)
        dx2 = np.sqrt(dx2)

        jacobian.append(dx1)
        seidel.append(dx2)

    fig, ax = plt.subplots()
    ax.plot(x, jacobian, color='green', label="Jacobian")
    ax.plot(x, seidel, color='purple', label="Seidel")
    ax.set(xlabel='x', ylabel='f', title='Erf')
    ax.grid()
    ax.legend()

    plt.show()


if __name__ == '__main__':
    #Пример Макса работает отлично
    # a = np.array([[10.0, -1.0, 2.0, 0.0],
    #               [-1.0, 11.0, -1., 3.0],
    #               [2.0, -1.0, 10.0, -1.0],
    #               [0.0, 3.0, -1.0, 8.0]])
    # b = np.array([6.0, 25.0, -11.0, 15.0])

    #Все ломается, решения вообще не совпадают
    a = np.array([[1.0, 1.0, -7.0, -1.0],
                  [4.0, 1.0, 2.0, -1.0],
                  [3.0, 0.0, -4.0, -1.0],
                  [1.0, 1.0, 0.0, 3.0]])
    b = np.array([6.0, 0.0, 6.0, 3.0])

    #Тут вообще лютая дичь с графиками ошибки и снова сломанное решение
    # a = np.array([[4.0, 1.0, 2.0, 0.5, 2.0],
    #               [1.0, 0.5, 0.0, 0.0, 0.0],
    #               [2.0, 0.0, 3.0, 0.0, 0.0],
    #               [0.5, 0.0, 0.0, 0.625, 0.0],
    #               [2.0, 0.0, 0.0, 0.0, 16.0]])
    # b = np.array([17.0, 3.0, 7.0, 6.0, 12.0])
    print("Jacob: ")
    print(solve_jacobi(a, b, 200))
    print("Seidel: ")
    print(solve_seidel(a, b, 200))
    print("Linalg: ")
    print(np.linalg.solve(a, b))
    draw_function(a, b)
