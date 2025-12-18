import unittest
import math

from integrator import *


class IntegratorTest(unittest.TestCase):
    def test1(self):
        """
        Tests integration of sine
        function with different steps.
        """
        self.assertAlmostEqual(
            integrate(
                math.sin, 2*math.pi, math.pi, steps=1000
            ),
            2,
            delta=0.001
        )
        self.assertAlmostEqual(
            integrate(
                math.sin, 2*math.pi, math.pi, steps=10000
            ),
            2,
            delta=0.001
        )

    def test2(self):
        """
        Tests multithreading integration of sine
        function with different steps.
        """
        self.assertAlmostEqual(
            integrateAsync(
                math.sin, 2*math.pi, math.pi, steps=1000
            ),
            2,
            delta=0.001
        )
        self.assertAlmostEqual(
            integrateAsync(
                math.sin, 2*math.pi, math.pi, steps=10000
            ),
            2,
            delta=0.001
        )

    def test3(self):
        """
        Tests multiprocessing integration of sine
        function with different steps.
        """
        self.assertAlmostEqual(
            integrateProcessAsync(
                math.sin, 2*math.pi, math.pi, steps=1000
            ),
            2,
            delta=0.001
        )
        self.assertAlmostEqual(
            integrateProcessAsync(
                math.sin, 2*math.pi, math.pi, steps=10000
            ),
            2,
            delta=0.001
        )

    def test4(self):
        """
        Tests simple integration of quadratic
        function with different steps.
        """
        def quadratic(x):
            return x ** 2

        self.assertAlmostEqual(
            integrate(quadratic, 0, 1, steps=1000),
            1 / 3,
            delta=0.001
        )
        self.assertAlmostEqual(
            integrate(quadratic, 0, 1, steps=10000),
            1 / 3,
            delta=0.001
        )

    def test5(self):
        """
        Tests simple integration of constant
        function with different steps.
        """
        def constant(x):
            return 5.0

        self.assertAlmostEqual(
            integrate(constant, 0, 2, steps=100),
            10.0,
            delta=0.001
        )

    def test6(self):
        """
        Tests multithreading integration to be equal to
        the simple one.
        """
        def test_func(x):
            return math.sin(x) * math.exp(-x)

        result_2 = integrateAsync(test_func, 0, 10,
                                  steps=10000, jobs=2)
        result_4 = integrateAsync(test_func, 0, 10,
                                  steps=10000, jobs=4)
        result_seq = integrate(test_func, 0, 10,
                               steps=10000)

        self.assertAlmostEqual(result_2, result_seq, delta=0.001)
        self.assertAlmostEqual(result_4, result_seq, delta=0.001)


if __name__ == "__main__":
    """
    Entry point
    """
    unittest.main(verbosity=2)
