import numpy as np

def read_forest(path):
    """ Reads a forest map at "path" """
    pass

def parse_forest(lines):
    """ Parses a forest from a list of row strings """
    def convert_line_to_int(line):
        tr = str.maketrans(".#", "01")
        return [int(d) for d in line.translate(tr)]
    return np.array([convert_line_to_int(l) for l in lines])

def is_a_tree(forest, x, y):
    """ Check if x, y coordinates in forest is a tree """
    pass
