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


def count_by_payment_type(df):
    """Returns a dictionary of counts by payment type."""
    return df['payment_type'].value_counts().to_dict()


def apply_discount(df, discount_rate=0.10):
    """Applies a discount to total price for gold customers."""
    df = df.copy()
    mask = df['customer_type'] == 'gold'
    df.loc[mask, 'total'] = df.loc[mask, 'total'] * (1 - discount_rate)
    return df
