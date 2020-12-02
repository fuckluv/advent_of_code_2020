import unittest
import pandas as pd
from day2_solution import read_input


class TestReadInput(unittest.TestCase):

    def test_read_input(self):
        test_input = read_input("./test_input.txt")
        expected = pd.DataFrame({
            "min_char": [1, 1, 2],
            "max_char": [3, 3, 9],
            "char": ["a", "b", "c"],
            "password": ["abcde", "cdefg", "ccccccccc"]
        })
        self.assertTrue((test_input.columns == expected.columns).all())
        self.assertTrue((test_input.values == expected.values).all())

class TestInputPolicy(unittest.TestCase):

    def test_input_policy(self):
        pass

if __name__ == '__main__':
    unittest.main()
