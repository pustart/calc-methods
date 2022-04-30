a = [[10.8000, 0.0475, 0, 0],
     [0.0321, 9.9000, 0.0523, 0],
     [0, 0.0369, 9.0000, 0.0570],
     [0, 0, 0.0416, 8.1000]]

b = [12.1430, 13.0897, 13.6744, 13.8972]
# x1 = 1,118587
# x2 = 1,310623
# x3 = 1,503186
# x4 = 1,707983


def is_correct_matrix(a):
    n = len(a)

    for row in range(0, n):
        if len(a[row]) != n:
            print('The matrix is not square')
            return False

    # for row in range(1, n - 1):
    #     if abs(a[row][row]) < abs(a[row][row - 1]) + abs(a[row][row + 1]):
    #         print('Diagonal dominance condition not met')
    #         return False
    #
    # if (abs(a[0][0]) < abs(a[0][1])) or (abs(a[n - 1][n - 1]) < abs(a[n - 1][n - 2])):
    #     print('Diagonal dominance condition not met')
    #     return False

    for row in range(0, len(a)):
        if a[row][row] == 0:
            print('Zero elements on the main diagonal')
            return False
    return True


def sweep_method(a, b):
    if not is_correct_matrix(a):
        print('Ошибка в исходных данных')
        return -1

    n = len(a)
    x = [0 for k in range(0, n)]

    # Straight stroke
    alpha_coef = [0 for k in range(0, n)]
    beta_coef = [0 for k in range(0, n)]

    alpha_coef[0] = -a[0][1] / a[0][0]
    beta_coef[0] = b[0] / a[0][0]

    for i in range(1, n - 1):
        alpha_coef[i] = -a[i][i + 1] / (a[i][i] + a[i][i - 1] * alpha_coef[i - 1])
        beta_coef[i] = (b[i] - a[i][i - 1] * beta_coef[i - 1]) / (a[i][i] + a[i][i - 1] * alpha_coef[i - 1])

    alpha_coef[n - 1] = 0
    beta_coef[n - 1] = (b[n - 1] - a[n - 1][n - 2] * beta_coef[n - 2]) / (a[n - 1][n - 1] + a[n - 1][n - 2] * alpha_coef[n - 2])

    # print('Sweep coefficients alpha_coef: ')
    # print(alpha_coef)
    # print('Sweep coefficients beta_coef: ')
    # print(beta_coef)

    # Reverse stroke
    x[n - 1] = beta_coef[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = alpha_coef[i - 1] * x[i] + beta_coef[i - 1]
    print(x)
    return x


def print_matrix(tr_matrix):
    for i in range(len(tr_matrix)):
        print("[", end="")
        for j in range(len(tr_matrix[i])):
            print("{", end="")
            print(tr_matrix[i][j], end="},")
        print("]")


if __name__ == '__main__':
    print_matrix(a)
    x = sweep_method(a, b)
    print("Solution: ")
    print(x)
