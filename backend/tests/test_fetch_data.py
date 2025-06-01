import pytest
from unittest.mock import patch
import pandas as pd
from app import fetch_data


@patch("app.fetch_data.requests.get")
def test_fetch_daily_returns_dataframe(mock_get):
    # Mock response structure from Alpha Vantage
    mock_response = {
        "Time Series (Daily)": {
            "2025-01-01": {
                "1. open": "100.0",
                "2. high": "110.0",
                "3. low": "90.0",
                "4. close": "105.0",
                "5. volume": "1234567"
            }
        }
    }

    # Mock the .json() method to return our fake response
    mock_get.return_value.json.return_value = mock_response

    df = fetch_data.fetch_daily("AAPL", outputsize="compact")

    assert isinstance(df, pd.DataFrame)
    assert "Open" in df.columns
    assert df.loc["2025-01-01", "Close"] == 105.0
