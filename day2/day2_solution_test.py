import unittest
import pandas as pd
from day2_solution import read_input, is_policy_compliantA

def get_test_df():
    return pd.DataFrame({
            "min_char": [1, 1, 2],
            "max_char": [3, 3, 9],
            "char": ["a", "b", "c"],
            "password": ["abcde", "cdefg", "ccccccccc"]
        })

class TestReadInput(unittest.TestCase):

    def test_read_input(self):
        test_input = read_input("./test_input.txt")
        expected = get_test_df()
        self.assertTrue((test_input.columns == expected.columns).all())
        self.assertTrue((test_input.values == expected.values).all())

class TestInputPolicyA(unittest.TestCase):

    def test_input_policyA(self):
        actual = get_test_df().apply(is_policy_compliantA, axis = 1).values
        expected = [True, False, True]
        self.assertTrue((actual == expected).all())

if __name__ == '__main__':
    unittest.main()
