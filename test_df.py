import pandas as pd

def test_df_cols():
    df_length = 10
    df = pd.read_csv("data/sales.csv")
    assert len(df.columns) == df_length
