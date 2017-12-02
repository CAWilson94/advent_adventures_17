import pandas as pd


def input_from_file(file_name):
    """ getting output from file input """
    data = pd.read_csv(file_name, delimiter='\s+', header = None)
    df = pd.DataFrame(data).fillna(0)
    return df

