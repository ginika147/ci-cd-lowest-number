# test_find_lowest_number.py
# StAuth10244: I Ginika Calistus Ezeh, 000932941 certify that this material is my original work.

import unittest
import tempfile
import os
from find_lowest_number import find_lowest_number_in_file

class TestLowestFinder(unittest.TestCase):

    def create_temp_file(self, contents):
        temp = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        temp.write(contents)
        temp.seek(0)
        temp.close()
        return temp.name

    def test_all_positive(self):
        filename = self.create_temp_file("20\n11\n55\n3\n")
        self.assertEqual(find_lowest_number_in_file(filename), 3.0)
        os.remove(filename)

    def test_with_negatives(self):
        filename = self.create_temp_file("-4\n-12\n7\n0\n")
        self.assertEqual(find_lowest_number_in_file(filename), -12.0)
        os.remove(filename)

    def test_all_equal(self):
        filename = self.create_temp_file("5\n5\n5\n")
        self.assertEqual(find_lowest_number_in_file(filename), 5.0)
        os.remove(filename)

    def test_one_element(self):
        filename = self.create_temp_file("99\n")
        self.assertEqual(find_lowest_number_in_file(filename), 99.0)
        os.remove(filename)

    def test_empty_file(self):
        filename = self.create_temp_file("")
        self.assertEqual(find_lowest_number_in_file(filename), "No numbers found in file")
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
