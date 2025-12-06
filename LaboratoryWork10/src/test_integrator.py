import unittest
from math import log, e

from integrator import integrate
from benchmark import printScore


def testEqual(obj: "IntegratorTest", a: float, b: float):
    res = abs(a - b)
    obj.assertLessEqual(res, 1)


class IntegratorTest (unittest.TestCase):
    def test1(self):
        testEqual(
            self,
            integrate(lambda x: 1 / x, e ** 10, e ** 20, steps=10 ** 6),
            10
        )

    def test2(self):
        testEqual(
            self,
            integrate(lambda x: 1 / x, 1, e ** 100, steps=10 ** 6),
            100
        )

    def test3(self):
        with self.assertRaises(TypeError):
            testEqual(self,
                      integrate(lambda x: x + 1, "50", 100),
                      625)


if __name__ == "__main__":
    printScore()
    unittest.main()