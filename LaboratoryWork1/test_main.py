import unittest
from searcher import *


class TestMath(unittest.TestCase):
    def test1STD(self):
        self.assertEqual(Searcher.searchTwoWithSum([1, 2, 2, 1, 5], 3), [0, 1])

    def test2WrongInputValue(self):
        self.assertEqual(Searcher.searchTwoWithSum([], 1, True), None)

    def test3WrongInputValue(self):
        with self.assertRaises(SearcherInputValueError):
            Searcher.searchTwoWithSum([], 5)

    def test4WrongInputValue(self):
        with self.assertRaises(SearcherInputValueError):
            Searcher.searchTwoWithSum([], 5)

    def test5WrongInputValue(self):
        with self.assertRaises(SearcherInputValueError):
            Searcher.searchTwoWithSum([1], 5)

    def test6WrongInputType(self):
        self.assertEqual(Searcher.searchTwoWithSum((1, 2, 3), 3, True), None)

    def test7WrongInputType(self):
        with self.assertRaises(SearcherInputTypeError):
            Searcher.searchTwoWithSum((1, 2, 3), 3)

    def test8WrongInputType(self):
        with self.assertRaises(SearcherInputTypeError):
            Searcher.searchTwoWithSum([1, 2, "4"], 3)

    def test9WrongInputType(self):
        with self.assertRaises(SearcherInputTypeError):
            Searcher.searchTwoWithSum([1, 2.6, 3], 4)

    def test10WrongInputType(self):
        with self.assertRaises(SearcherInputTypeError):
            Searcher.searchTwoWithSum([1, 2, 3], "3")

    def test11STD(self):
        self.assertEqual(Searcher.searchTwoWithSum([1, 2, 2, 1, 5, 2], 4), [1, 2])



if "__name__" == "__main__":
    unittest.main()
