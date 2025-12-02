import unittest
from Test1 import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()
