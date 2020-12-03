import unittest
from solution_day3 import *
import importlib

class TestParseForest(unittest.TestCase):

    def testInput(self):
        input_arr = parse_forest([".#.","..#", "###"])
        expected_arr = np.array([[0, 1, 0], [0, 0 , 1], [1, 1, 1]])
        self.assertTrue(type(input_arr) is np.ndarray)
        self.assertTrue((input_arr == expected_arr).all())

if __name__ == "__main__":
    # importlib.reload(solution_day3)
    unittest.main()
