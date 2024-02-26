import unittest
from main import prime_number

class TestPrimeNumber(unittest.TestCase):

    def test_small_primes(self):
        self.assertEqual(prime_number(2), True, "2 is a prime number")
        self.assertEqual(prime_number(3), True, "3 is a prime number")
        self.assertEqual(prime_number(5), True, "5 is a prime number")
        self.assertEqual(prime_number(7), True, "7 is a prime number")

    def test_small_non_primes(self):
        self.assertEqual(prime_number(4), False, "4 is not a prime number")
        self.assertEqual(prime_number(6), False, "6 is not a prime number")
        self.assertEqual(prime_number(8), False, "8 is not a prime number")
        self.assertEqual(prime_number(9), False, "9 is not a prime number")

    def test_large_primes(self):
        self.assertEqual(prime_number(1000000007), True, "1000000007 is a prime number")
        self.assertEqual(prime_number(1500450271), True, "1500450271 is a prime number")
        self.assertEqual(prime_number(10000000019), True, "10000000019 is a prime number")
        self.assertEqual(prime_number(10000000033), True, "10000000033 is a prime number")

    def test_large_non_primes(self):
        self.assertEqual(prime_number(1000000000), False, "1000000000 is not a prime number")
        self.assertEqual(prime_number(10000000010), False, "10000000010 is not a prime number")
        self.assertEqual(prime_number(10000000025), False, "10000000025 is not a prime number")

    def test_zero_and_one(self):
        self.assertEqual(prime_number(0), False, "0 is not a prime number")
        self.assertEqual(prime_number(1), False, "1 is not a prime number")

if __name__ == '__main__':
    unittest.main()