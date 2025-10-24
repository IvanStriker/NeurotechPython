import unittest
import io
import requests

from currency import get_currencies
from decorators import trace

# Тесты
class TestStreamWrite(unittest.TestCase):

    def TestStreamWrite(self):
        super()
        self.raisedCounting = 0

    def setUp(self):
        self.nonstandardstream = io.StringIO()
        self.trace = trace(get_currencies, handle=self.nonstandardstream)

    def test_writing_stream(self):
        with self.assertRaises(requests.exceptions.RequestException):
            self.get_currencies = self.trace(
                ['USD'],
                url="https://",
                handle=self.nonstandardstream
            )
            self.raisedCounting += 1
            self.assertEqual(
                self.nonstandardstream.getvalue().count(
                    "Ошибка при запросе к API: "),
                self.raisedCounting)
    # self.trace(['USD'], url="https://")

    def tearDown(self):
        del self.nonstandardstream
