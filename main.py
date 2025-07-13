import pandas as pd


def load_sample_data(path="sales.csv"):
    """
    Reads a CSV file and drops the 'Unnamed: 0' column.
    """
    df = pd.read_csv(path).drop(columns=["Unnamed: 0"])
    return df


def total_sales(df):
    return df["total"].sum()


def unique_customers(df):
    return df["customer_type"].nunique()


def average_price(df):
    return round(df["unit_price"].mean(), 2)


def get_by_category(df, category):
    return df[df["category"] == category]
