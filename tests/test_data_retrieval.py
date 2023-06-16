"""Unit test: Core data retrieval function"""

from src.data.pre_processor import retrieve_bitcoin_data


def test_retrieve_bitcoin_data():
    """
    Test the retrieve_bitcoin_data function.

    This test case retrieves USD rate data for the past 1440 minutes (1 day)
    and verifies that the result is not empty.
    """
    result = retrieve_bitcoin_data(rate_type="usd_rate", time_range=(1440,))

    assert len(result) > 0
