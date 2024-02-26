import unittest
from main import join_array_remove_duplicat

class TestJoinArrayRemoveDuplicate(unittest.TestCase):

    def test_no_duplicates(self):
        result = join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"])
        expected = ["apel", "anggur", "lemon", "leci", "nanas"]
        self.assertEqual(result, expected)

    def test_with_duplicates(self):
        result = join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"])
        expected = ["samsung", "apple", "sony", "xiaomi"]
        self.assertEqual(result, expected)

    def test_same_elements(self):
        result = join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"])
        expected = ["football", "basketball"]
        self.assertEqual(result, expected)

    def test_empty_arrays(self):
        result = join_array_remove_duplicate([], [])
        expected = []
        self.assertEqual(result, expected)

    def test_one_empty_array(self):
        result = join_array_remove_duplicate(["apple", "banana"], [])
        expected = ["apple", "banana"]
        self.assertEqual(result, expected)

    def test_with_duplicates_and_empty(self):
        result = join_array_remove_duplicate(["apple", "banana", "banana", "cherry"], ["cherry", "date", "date"])
        expected = ["apple", "banana", "cherry", "date"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()