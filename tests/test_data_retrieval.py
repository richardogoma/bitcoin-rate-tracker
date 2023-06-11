from etl.extract.data import retrieve_rates
from config import Config


def test_retrieve_rates():
    result = "time" in retrieve_rates(uri=Config.API_URI)
    assert True == result
