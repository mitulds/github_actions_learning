import pandas as pd

df = pd.read_csv("sales.csv").drop(columns=['Unnamed: 0'])
print(len(df.columns))
