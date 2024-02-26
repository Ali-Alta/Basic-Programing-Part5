import unittest
from main import pair_sum

class TestPairSum(unittest.TestCase):

    def test_example_1(self):
        result = pair_sum([1, 2, 3, 4, 6], 6)
        expected = [1, 3]
        self.assertEqual(result, expected)

    def test_example_2(self):
        result = pair_sum([2, 5, 9, 11], 11)
        expected = [0, 2]
        self.assertEqual(result, expected)

    def test_example_3(self):
        result = pair_sum([1, 3, 5, 7], 12)
        expected = [2, 3]
        self.assertEqual(result, expected)

    def test_example_4(self):
        result = pair_sum([1, 4, 6, 8], 10)
        expected = [1, 2]
        self.assertEqual(result, expected)

    def test_example_5(self):
        result = pair_sum([1, 5, 6, 7], 6)
        expected = [0, 1]
        self.assertEqual(result, expected)

    def test_no_pair(self):
        result = pair_sum([1, 2, 3, 4, 6], 11)
        expected = None
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()