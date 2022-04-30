class CSR(object):
    def __init__(self, n, m, value_arr, col_arr, row_arr):
        self.n = n
        self.m = m
        self.value_arr = value_arr
        self.col_arr = col_arr
        self.row_arr = row_arr

    def __str__(self):
        return "x: {0} y: {1}".format(self.x, self.y)

    @staticmethod
    def parse_matrix_to_csr(matrix):
        values = []
        columns = []
        rows = [0]
        for i in range(len(matrix)):
            rows_counter = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    values.append(matrix[i][j])
                    columns.append(j)
                    rows_counter += 1
            rows.append(rows[i] + rows_counter)
        return CSR(len(matrix), len(matrix[0]), values, columns, rows)

    @staticmethod
    def parse_csr_to_matrix(csr):

        matrix = [[0] * csr.m for i in range(csr.n)]
        for i in range(len(csr.value_arr)):
            n = CSR.__find_row(i, csr.row_arr)
            matrix[n][csr.col_arr[i]] = csr.value_arr[i]
        return matrix

    @staticmethod
    def __find_row(i, arr_row):
        n = 0
        for n in range(len(arr_row) - 1):
            if arr_row[n + 1] >= i + 1:
                return n
        return -1
