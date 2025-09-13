import unittest
from main import searchingTwo


class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(searchingTwo([1, 2, 3, 4, 5], 3), [0, 1])


if "__name__" == "__main__":
    unittest.main()
