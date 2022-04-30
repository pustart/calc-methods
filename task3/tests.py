import unittest
from task3._task3 import *
import numpy as np


class TestSweepMethods(unittest.TestCase):
    def test_matrix1(self):
        a = [[10.8000, 0.0475, 0, 0],
             [0.0321, 9.9000, 0.0523, 0],
             [0, 0.0369, 9.0000, 0.0570],
             [0, 0, 0.0416, 8.1000]]

        b = [12.1430, 13.0897, 13.6744, 13.8972]
        print(np.linalg.solve(a, b))
        np.testing.assert_almost_equal(sweep_method(a, b), np.linalg.solve(a, b))

    def test_matrix2(self):
        a = [[2.0, 1.0, 0, 0],
             [1.0, 10.0, -5.0, 0],
             [0, 0.0, -5.0, 2.0],
             [0, 0, 1.0, 4.0]]

        b = [-5, -18, -40, -27]
        print(np.linalg.solve(a, b))
        np.testing.assert_almost_equal(sweep_method(a, b), np.linalg.solve(a, b), 10)

    def test_matrix3(self):
        a = [[3.0, -2.0, 0, 0, 0],
             [1.0, 4.0, -3.0, 0, 0],
             [0, -3.0, 8.0, -4.0, 0],
             [0, 0, -2.0, 5.0, -2.0],
             [0, 0.0, 0.0, 0.0, 1]]

        b = [-9, 5, -9, 6, 5]
        print(np.linalg.solve(a, b))
        np.testing.assert_almost_equal(sweep_method(a, b), np.linalg.solve(a, b), 10)


if __name__ == '__main__':
    unittest.main()
