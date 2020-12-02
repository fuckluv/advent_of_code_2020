import pandas as pd

def read_input(path):
    df_input = pd.read_csv(
        path,
        sep = '-|\s+|:\s',
        engine = 'python',
        names = ['min_char', 'max_char', 'char', 'password']
    )
    return df_input
