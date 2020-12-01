import unittest
from day1_solution import *

class TestPairGivenSum(unittest.TestCase):

    def test_values(self):
        self.assertEqual(
           find_pair_given_sum([1721, 979, 366, 299, 675, 1456], 2020),
           (0, 3)
        )
        self.assertIsNone(find_pair_given_sum([1010], 2020))
        self.assertIsNone(find_pair_given_sum([0, 0, 0], 2020))

    def test_emptylist(self):
        self.assertIsNone(find_pair_given_sum([], 2020))


class TestTrioGivenSum(unittest.TestCase):

    def test_values(self):
        self.assertEqual(
           find_trio_given_sum([1721, 979, 366, 299, 675, 1456], 2020),
           (1, 2, 4)
        )
        self.assertIsNone(find_trio_given_sum([1000, 20], 2020))
        self.assertIsNone(find_trio_given_sum([0, 0, 0], 2020))

    def test_shortlist(self):
        self.assertIsNone(find_trio_given_sum([], 2020))
        self.assertIsNone(find_trio_given_sum([2020], 2020))

if __name__ == '__main__':
    unittest.main()
