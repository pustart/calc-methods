from task3.CSR import CSR

a = [[10.8000, 0.0475, 0, 0],
     [0.0321, 9.9000, 0.0523, 0],
     [0, 0.0369, 9.0000, 0.0570],
     [0, 0, 0.0416, 8.1000]]


def print_matrix(tr_matrix):
    for i in range(len(tr_matrix)):
        print("[", end="")
        for j in range(len(tr_matrix[i])):
            print("{", end="")
            print(tr_matrix[i][j], end="},")
        print("]")


if __name__ == '__main__':
    print_matrix(a)
    print("-------------")
    csr = CSR.parse_matrix_to_csr(a)
    mtrx = CSR.parse_csr_to_matrix(csr)
    print_matrix(mtrx)
