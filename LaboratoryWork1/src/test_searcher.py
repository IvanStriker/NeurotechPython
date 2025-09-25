import unittest
from searcher import *


class TestSearcher(unittest.TestCase):
    """
    This class contains all the tests for Searcher.searchTwoWithSum
    method.
    'STD' tests are to check if the base algorithm works.
    'WrongInputValue' tests are to check if len(nums) >= 2
    'WrongInputType' tests are to check if the types of arguments
    are valid: nums (List[int]), target (int)
    These methods also verify if noexcept arg has its effect:
    when other inputs given are incorrect, the function being tested
    is to raise an error if noexcept = False and to return None
    if noexcept = True.
    """

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
        self.assertEqual(Searcher.searchTwoWithSum([1, 2.6, 3], 4, True), None)

    def test11WrongInputType(self):
        with self.assertRaises(SearcherInputTypeError):
            Searcher.searchTwoWithSum([1, 2, 3], "3")

    def test12STD(self):
        self.assertEqual(Searcher.searchTwoWithSum([1, 2, 2, 1, 5, 2], 4), [1, 2])

    def test13STD(self):
        self.assertEqual(Searcher.searchTwoWithSum([1, 2, 2, 1, 5, 2, 8, 19, 34, -5, 0, -1, -11], 8), [6, 10])


if "__name__" == "__main__":
    unittest.main()
