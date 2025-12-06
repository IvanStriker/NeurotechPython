import unittest
import io

import requests

from currency import get_currencies
from decorators import logger


class TestGetCurrenciesApi(unittest.TestCase):
    """
    Tests whether the api itself works or not
    """

    def testBasic(self):
        lst = ['AUD', 'AZN', 'DZD']
        curs = get_currencies(lst)
        for item in lst:
            self.assertIn(item, curs)
            self.assertTrue(isinstance(curs[item], int | float))

    def testRaises(self):
        with self.assertRaises(
                requests.exceptions.ConnectionError):
            get_currencies(['AUD', 'AZN', 'DZD'], url="http://")

        with self.assertRaises(KeyError):
            get_currencies(["You won't find!"])


def power(a: int, b: int) -> int:
    """
    Counts a^b if a, b are integers

    Raises:
        ValueError: in case a or b isn't an instance
            of int
    Returns:
        int: a^b
    """
    if not isinstance(b, int):
        raise ValueError(f"Invalid argument: {b}")
    if not isinstance(a, int):
        raise ValueError(f"Invalid argument: {a}")
    if b == 0:
        return 1
    if b % 2 == 0:
        return power(a, b // 2) ** 2
    return power(a, b - 1) * a


class TestLogger(unittest.TestCase):
    """
    Tests whether the logging decorator works or not
    """

    def setUp(self):
        """
        Prepares inner variables for testing
        """
        self.stream = io.StringIO()
        self.trace = logger(power, handle=self.stream)

    def testBasic(self):
        self.trace(2, 10)
        self.assertIn("Calling", self.stream.getvalue())
        self.assertIn("successfully", self.stream.getvalue())

    def testRaises(self):
        with self.assertRaises(ValueError):
            self.trace(2, "10")
            self.assertIn("Invalid argument:",
                          self.stream.getvalue())

    def testRaises2(self):
        with self.assertRaises(ValueError):
            self.trace(2.4, 3)
            self.assertIn("Invalid argument: 2.4",
                          self.stream.getvalue())


    def tearDown(self):
        """
        Cancels resources
        """
        del self.stream


class TestStreamWrite(unittest.TestCase):
    """
    Tests whether the logging decorator works or not
    when it's provided with a resource
    """

    def setUp(self):
        """
        Prepares inner variables for testing
        """
        self.nonStandardStream = io.StringIO()
        self.raisedCounting = 0
        self.trace = logger(get_currencies, handle=self.nonStandardStream)

    def test_writing_stream(self):
        with self.assertRaises(requests.exceptions.RequestException):
            self.get_currencies = self.trace(
                ['USD'],
                url="https://"
            )
            self.raisedCounting += 1
            # self.assertIn("Ошибка при запросе к API: ", self.nonStandardStream.getvalue())
            self.assertEqual(
                self.nonStandardStream.getvalue().count(
                    "!!"),
                self.raisedCounting)

    # self.trace(['USD'], url="https://")

    def tearDown(self):
        """
        Cancels the resources
        """
        del self.nonStandardStream


if __name__ == "__main__":
    unittest.main(verbosity=2)
