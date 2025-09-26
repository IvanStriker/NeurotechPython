import unittest
from guesser import Guesser


class GuesserTest (unittest.TestCase):
    """A simple class for testing"""
    def test1(self):
        self.assertEqual(Guesser.guess(
            3,
            []
        ), (None, 0))

    def test2(self):
        self.assertEqual(Guesser.guess(
            3,
            [],
            method="lin"
        ), (None, 0))

    def test3(self):
        self.assertEqual(Guesser.guess(
            3,
            [1, 3, 5, 6, 3, 2]
        ), (3, 1))

    def test4(self):
        self.assertEqual(Guesser.guess(
            3,
            [1, 3, 5, 6, 3, 2],
            method="lin"
        ), (3, 3))

    def test5(self):
        self.assertEqual(Guesser.guess(
            5,
            [1, 3, 5, 6, 3, 2]
        ), (5, 2))

    def test6(self):
        self.assertEqual(Guesser.guess(
            5,
            [1, 3, 5, 6, 3, 2],
            method="lin"
        ), (5, 5))

    def test7(self):
        self.assertEqual(Guesser.guess(
            5,
            [5],
        ), (5, 1))


if __name__ == "__main__":
    unittest.main()
