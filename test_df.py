import main
import pytest

@pytest.mark.xfail
def test_df_cols():
    df = main.load_sales_data()
    assert not df.empty
    assert len(df.columns) == 10
