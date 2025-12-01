import unittest
from find_lowest_number import find_lowest_number_in_list

class TestLowestFinder(unittest.TestCase):

    def test_all_positive(self):
        self.assertEqual(find_lowest_number_in_list([20, 11, 55, 3]), 3)

    def test_with_negatives(self):
        self.assertEqual(find_lowest_number_in_list([-4, -12, 7, 0]), -12)

    def test_all_equal(self):
        self.assertEqual(find_lowest_number_in_list([5, 5, 5]), 5)

    def test_one_element(self):
        self.assertEqual(find_lowest_number_in_list([99]), 99)

if __name__ == '__main__':
    unittest.main()
