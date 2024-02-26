import unittest
from main import pow

class TestPowFunction(unittest.TestCase):

    def test_pow_example_1(self):
        self.assertEqual(pow(2, 3), 8)

    def test_pow_example_2(self):
        self.assertEqual(pow(7, 2), 49)

    def test_pow_example_3(self):
        self.assertEqual(pow(10, 5), 100000)

    def test_pow_example_4(self):
        self.assertEqual(pow(17, 6), 24137569)

    def test_pow_example_5(self):
        self.assertEqual(pow(5, 3), 125)

    def test_pow_with_zero_exponent(self):
        self.assertEqual(pow(7, 0), 1)

    def test_pow_with_negative_exponents(self):
        self.assertEqual(pow(3, -2), 1/9)

if __name__ == '__main__':
    unittest.main()