import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
    def load(path: str) -> pd.DataFrame
    Load with pandas lib a comma-separated values csv file and return it into
    a pandas.DataFrame
    '''
    try:
        # With column for row index
        # data = pd.read_csv(path)
        # Without column for row index
        data = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", data.shape)
        return data
    except Exception as e:
        print("AssertionError:", e)
