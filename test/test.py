"""
In this file you may have your tests

"""
import unittest
import scipy as sp
import sys
sys.path.append('../lorenz')
from solver import compute_states


class TestComputeStates(unittest.TestCase):

    def test_zero_output(self):
        self.assertEqual(compute_states(0, 0, 0, 0, 0, 0, 1, 0.01),
                         (sp.array([[0.]]), sp.array([[0.]]),
                          sp.array([[0.]])))

        self.assertEqual(compute_states(0, 0, 0, 10, 8./3, 6, 1, 0.01),
                         (sp.array([[0.]]), sp.array([[0.]]),
                          sp.array([[0.]])))

    def test_initial_conditions(self):
        self.assertEqual(compute_states(0.01, 0, 0, 0, 0, 0, 1, 0.01),
                         (sp.array([[0.01]]), sp.array([[0.]]),
                          sp.array([[0.]])))

        self.assertEqual(compute_states(0.01, 0, 0, 10, 8./3, 6, 1, 0.01),
                         (sp.array([[0.01]]), sp.array([[0.]]),
                          sp.array([[0.]])))

    def test_known_outputs(self):
        # First iteration of x
        self.assertEqual(compute_states(
                         0.01, 0, 0, 10, 8./3, 6, 2, 0.01)[0][1],
                         sp.array([0.01 + 0.01 * (10 * (0 - 0.01))]))

        # First iteration of y
        self.assertEqual(compute_states(
                         0.01, 0, 0, 10, 8./3, 6, 2, 0.01)[1][1],
                         sp.array([0 + 0.01 * (0.01 * (6 - 0) - 0)]))

        # First iteration of z
        self.assertEqual(compute_states(
                         0.01, 0, 0, 10, 8./3, 6, 2, 0.01)[2][1],
                         sp.array([0 + 0.01 * (0.01 * 0 - (8./3 * 0))]))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestComputeStates)
    unittest.TextTestRunner(verbosity=2).run(suite)
