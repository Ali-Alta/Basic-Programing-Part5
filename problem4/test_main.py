import unittest
from main import muncul_sekali

class TestMunculSekali(unittest.TestCase):

    def test_example_1(self):
        result = muncul_sekali("1234123")
        expected = [4]
        self.assertEqual(result, expected)

    def test_example_2(self):
        result = muncul_sekali("76523752")
        expected = [6, 3]
        self.assertEqual(result, expected)

    def test_example_3(self):
        result = muncul_sekali("12345")
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)

    def test_example_4(self):
        result = muncul_sekali("1122334455")
        expected = []
        self.assertEqual(result, expected)

    def test_example_5(self):
        result = muncul_sekali("0872504")
        expected = [8, 7, 2, 5, 4]
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = muncul_sekali("")
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()