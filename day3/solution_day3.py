import numpy as np

def read_forest(path):
    """ Reads a forest map at "path" """
    with open(path) as f:
        forest = parse_forest(l.strip() for l in f)
        return(forest)

def parse_forest(lines):
    """ Parses a forest from a list of row strings """
    def convert_line_to_int(line):
        tr = str.maketrans(".#", "01")
        return [int(d) for d in line.translate(tr)]
    return np.array([convert_line_to_int(l) for l in lines])

def is_a_tree(forest, coords):
    """
    Check if coords  coordinates (list of tuples), first element is
    row, second is column, both 0 indexed) in forest is a tree
    """
    if type(coords) is not list:
        raise ValueError
    if len(coords) == 0:
        raise ValueError
    forest_width = forest.shape[1]
    if any([not 0 <= r < forest_width for r, _ in coords]):
        raise ValueError
    is_a_tree = [forest[r, c % forest_width] == 1 for r, c in coords]
    return is_a_tree
