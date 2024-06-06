import pandas as pd


def import_windpro_topography(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, sep=";", decimal=",", skiprows=1, header=None)
