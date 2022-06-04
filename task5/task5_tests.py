from task5.systems_solving import *
import unittest


class Testing(unittest.TestCase):
    def test_suitability1(self):
        a = np.array([[5, 2, 3],
                      [2, 6, 1],
                      [3, 1, 7]])
        b = np.array([[5], [7], [24]])
        message = "Matrices a, b are not suitable"
        self.assertTrue(is_system_suitable(a, b), message)

    def test_suitability2(self):
        a = np.array([[5, 2, 3],
                      [2, 6, 1],
                      [3, 1, 7]])
        b = np.array([[5], [7], [24], [0]])
        message = "Matrices a, b are suitable"
        self.assertFalse(is_system_suitable(a, b), message)

    def test_suitability3(self):
        a = np.array([[5, 2, 3],
                      [7, 6, 1],
                      [3, 1, 7]])
        b = np.array([[5], [7], [24]])
        message = "Matrices a, b are suitable"
        self.assertFalse(is_system_suitable(a, b), message)

    def test_jacobi1(self):
        a = np.array([[50, 15, 25, 13],
                      [15, 55, 22, 3],
                      [55, 225, 979, 6],
                      [4, 16, 28, 34]])
        b = np.array([5, 7, 24, 0])
        res_jacobi = solve_jacobi(a, b, 200)
        res_linalg = np.linalg.solve(a, b)
        np.testing.assert_almost_equal(res_linalg, res_jacobi)

    def test_jacobi2(self):
        a = np.array([[25, 15, -5],
                      [15, 18, 0],
                      [-5, 0, 11]])
        b = np.array([35, 33, 6])
        res_jacobi = solve_jacobi(a, b, 200)
        res_linalg = np.linalg.solve(a, b)
        np.testing.assert_almost_equal(res_linalg, res_jacobi, 1)  # only 1 decimal

    def test_seidel1(self):
        a = np.array([[25, 15, -5],
                      [15, 18, 0],
                      [-5, 0, 11]])
        b = np.array([35, 33, 6])
        res_seidel = solve_seidel(a, b, 200)
        res_linalg = np.linalg.solve(a, b)
        np.testing.assert_almost_equal(res_linalg, res_seidel, 5)  # 5 decimals

    def test_jacobi3(self):
        a = np.array([[10.0, -1.0, 2.0, 0.0],
                      [-1.0, 11.0, -1., 3.0],
                      [2.0, -1.0, 10.0, -1.0],
                      [0.0, 3.0, -1.0, 8.0]])
        b = np.array([6.0, 25.0, -11.0, 15.0])
        res_jacobi = solve_jacobi(a, b, 200)
        res_linalg = np.linalg.solve(a, b)
        np.testing.assert_almost_equal(res_linalg, res_jacobi, 5)

    def test_seidel2(self):
        a = np.array([[5, 2, 3],
                      [2, 6, 1],
                      [3, 1, 7]])
        b = np.array([5, 7, 24])
        res_seidel = solve_seidel(a, b, 200)
        res_linalg = np.linalg.solve(a, b)
        np.testing.assert_almost_equal(res_linalg, res_seidel, 5)

    def test_seidel3(self):
        a = np.array([[5, 2, 3],
                      [2, 6, 1],
                      [3, 1, 7]])
        b = np.array([10, 20, 30])
        res_seidel = solve_seidel(a, b, 200)
        res_linalg = np.linalg.solve(a, b)
        np.testing.assert_almost_equal(res_linalg, res_seidel, 5)

    def test_jacobi4(self):
        a = np.array([[5, 2, 3],
                      [2, 6, 1],
                      [3, 1, 7]])
        b = np.array([10, 20, 30])
        res_jacobi = solve_jacobi(a, b, 200)
        res_linalg = np.linalg.solve(a, b)
        np.testing.assert_almost_equal(res_linalg, res_jacobi, 5)
