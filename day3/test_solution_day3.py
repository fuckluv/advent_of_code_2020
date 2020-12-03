import unittest
from solution_day3 import *

class TestParseForest(unittest.TestCase):

    def test_input(self):
        input_arr = parse_forest([".#.","..#", "###"])
        expected_arr = np.array([[0, 1, 0], [0, 0 , 1], [1, 1, 1]])
        self.assertTrue(type(input_arr) is np.ndarray)
        self.assertTrue((input_arr == expected_arr).all())

class TestReadForest(unittest.TestCase):

    def test_input(self):
        input_arr = read_forest("./test_input.txt")
        self.assertEqual(input_arr.shape, (11, 11))

class TestIsATree(unittest.TestCase):

    def test_is_a_tree(self):
        input_arr = parse_forest([".#.","..#", "###"])
        self.assertEqual(is_a_tree(input_arr, [(0, 0)]), [False])
        self.assertEqual(is_a_tree(input_arr, [(0, 1)]), [True])
        self.assertTrue(
            all(is_a_tree(input_arr, [(2, 0), (2, 1)]))
        )

    def test_recycle_forest_left(self):
        input_arr = parse_forest([".#.","..#", "###"])
        self.assertEqual(is_a_tree(input_arr, [(0, -1)]), [False])
        self.assertEqual(is_a_tree(input_arr, [(0, -2)]), [True])
        self.assertEqual(is_a_tree(input_arr, [(1, -4)]), [True])
        self.assertEqual(is_a_tree(input_arr, [(1, -5)]), [False])
        self.assertTrue(all(is_a_tree(input_arr, [(0, -2), (1, -4)])))

    def test_recycle_forest_left(self):
        input_arr = parse_forest([".#.","..#", "###"])
        self.assertEqual(is_a_tree(input_arr, [(0, 5)]), [False])
        self.assertEqual(is_a_tree(input_arr, [(0, 4)]), [True])
        self.assertEqual(is_a_tree(input_arr, [(1, 8)]), [True])
        self.assertEqual(is_a_tree(input_arr, [(1, 7)]), [False])
        self.assertTrue(all(is_a_tree(input_arr, [(0, 4), (1, 8)])))

    def test_value(self):
        input_arr = parse_forest([".#.","..#", "###"])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, [(-1, 0)])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, [(3, 0)])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, [(0, 1), (3, 0)])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, [(-1, -1), (0, 0)])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, (-1, -1))

if __name__ == "__main__":
    unittest.main()
