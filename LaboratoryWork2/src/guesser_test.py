import unittest
from guesser import Guesser


class GuesserTest(unittest.TestCase):
    """A simple class for testing Guesser.guess"""

    def test1(self):
        """Testing bin algo with the empty array"""
        self.assertEqual(Guesser.guess(
            3,
            []
        ), (None, 0))

    def test2(self):
        """Testing lin algo with the empty array"""
        self.assertEqual(Guesser.guess(
            3,
            [],
            method="lin"
        ), (None, 0))

    def test3(self):
        """Testing bin algo with an unsorted array"""
        self.assertEqual(Guesser.guess(
            3,
            [1, 3, 5, 6, 3, 2]
        ), (3, 1))

    def test4(self):
        """Testing lin algo with an unsorted array"""
        self.assertEqual(Guesser.guess(
            3,
            [1, 3, 5, 6, 3, 2],
            method="lin"
        ), (3, 3))

    def test5(self):
        """Testing bin algo with an unsorted array"""
        self.assertEqual(Guesser.guess(
            5,
            [1, 3, 5, 6, 3, 2]
        ), (5, 2))

    def test6(self):
        """Testing lin algo with an unsorted array"""
        self.assertEqual(Guesser.guess(
            5,
            [1, 3, 5, 6, 3, 2],
            method="lin"
        ), (5, 5))

    def test7(self):
        """Testing bin algo with an array of 1 length"""
        self.assertEqual(Guesser.guess(
            5,
            [5],
        ), (5, 1))

    def test8(self):
        """Testing lin algo with an array of 1 length"""
        self.assertEqual(Guesser.guess(
            5,
            [5],
            method="lin"
        ), (5, 1))

    def test9(self):
        """Testing bin algo with a target out of the array"""
        self.assertEqual(Guesser.guess(
            5,
            [2, 3, 4]
        ), (None, 2))

    def test10(self):
        """Testing lin algo with a target out of the array"""
        self.assertEqual(Guesser.guess(
            5,
            [2, 3, 4],
            method="lin",
        ), (None, 3))

    def test11(self):
        """Testing with wrong type of target"""
        with self.assertRaises(TypeError):
            Guesser.guess(
                5.6,
                [2, 3, 4]
            )

    def test12(self):
        """Testing with elements: tuple"""
        with self.assertRaises(TypeError):
            Guesser.guess(
                5,
                (2, 3, 4)
            )

    def test13(self):
        """Testing with float values in elements"""
        with self.assertRaises(TypeError):
            Guesser.guess(
                5,
                [2.6, 3, 4]
            )

if __name__ == "__main__":
    unittest.main()
