from unittest.mock import patch, MagicMock
import pytest
pd = pytest.importorskip("pandas")
from app.fetch_data import fetch_daily

sample_response = {
    "Time Series (Daily)": {
        "2023-01-02": {
            "1. open": "10.0",
            "2. high": "12.0",
            "3. low": "9.5",
            "4. close": "11.0",
            "5. volume": "1000"
        }
    }
}

class MockResponse:
    def json(self):
        return sample_response

@patch('app.fetch_data.requests.get')
def test_fetch_daily_numeric(mock_get):
    mock_get.return_value = MockResponse()
    df = fetch_daily('MSFT')
    assert df.loc[pd.Timestamp('2023-01-02'), 'Open'] == 10.0
    assert df.dtypes['Open'] == float

