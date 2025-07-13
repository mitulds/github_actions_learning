# test_df.py

import pytest
from main import load_sample_data, total_sales, unique_customers, average_price, get_by_category

@pytest.fixture
def sample_df():
    return load_sample_data()

def test_total_sales(sample_df):
    assert total_sales(sample_df) == pytest.approx(12.35)

def test_unique_customers(sample_df):
    assert unique_customers(sample_df) == 3

def test_average_price(sample_df):
    assert average_price(sample_df) == 2.72  # (3.99 + 3.99 + 0.19)/3

def test_get_by_category(sample_df):
    fruit_df = get_by_category(sample_df, "fruit")
    assert len(fruit_df) == 3

@pytest.mark.xfail(reason="Category 'veg' not in sample data")
def test_get_by_nonexistent_category(sample_df):
    veg_df = get_by_category(sample_df, "veg")
    assert not veg_df.empty  # will fail on purpose
