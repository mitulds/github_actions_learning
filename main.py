import pandas as pd

def load_sales_data(path="sales.csv"):
    """
    Reads a CSV file and drops the 'Unnamed: 0' column.
    """
    df = pd.read_csv(path).drop(columns=["Unnamed: 0"])
    return df
