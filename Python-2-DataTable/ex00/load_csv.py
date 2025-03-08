import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    '''
    def load(path: str) -> DataFrame:
    Write the dimensions of the dataset and return it
    '''
    data = pd.read_csv(path, index_col=0)  # index_col=0 lit a partir de col 0 et skip rownames(number of lines) before each col
    print("Loading dataset of dimensions", data.shape)
    return data