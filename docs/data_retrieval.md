## Documentation: `retrieve_bitcoin_data` Function

The `retrieve_bitcoin_data` function is responsible for retrieving bitcoin rate data from a SQLite database for a specific rate type and time range. It takes two parameters, `rate_type` and `time_range`, and returns a list of dictionaries representing the retrieved data.

### Parameters

- `rate_type` (str): The type of bitcoin rate to retrieve. It can be one of the following:
  - `'usd_rate'`: Represents the USD (United States Dollar) rate for bitcoin.
  - `'gbp_rate'`: Represents the GBP (British Pound) rate for bitcoin.
  - `'eur_rate'`: Represents the EUR (Euro) rate for bitcoin.

- `time_range` (tuple): The time range in minutes for which to retrieve the bitcoin rate data. It should be a tuple with two elements:
  - `time_range[0]` (int): The number of minutes in the past from the current time.
  - `time_range[1]` (int): *(Not used in the function)* The number of minutes in the future from the current time.

### Return Value

The function returns a list of dictionaries representing the retrieved data. Each dictionary in the list corresponds to a row of data and contains two key-value pairs:
- `'timestamp'`: The timestamp of the bitcoin rate data point.
- `rate_type`: The value of the bitcoin rate for the specified `rate_type` (e.g., 'usd_rate') at the given timestamp.

### Usage

To use the `retrieve_bitcoin_data` function, make sure you have the required dependencies installed and imported. Then, call the function by providing the necessary arguments:

```python
rate_type = 'usd_rate'  # Example: Retrieve USD rate data
time_range = (60, 0)   # Example: Retrieve data for the past 60 minutes

data = retrieve_bitcoin_data(rate_type, time_range)
```

Make sure to replace `rate_type` and `time_range` with the desired values for your use case. The retrieved bitcoin rate data will be stored in the `data` variable as a list of dictionaries.

### Dependencies

The function relies on the following dependencies:
- `sqlite3`: The standard library module for SQLite database operations.
- `time`: The standard library module for time-related operations.
- `config`: A custom module that provides configuration settings for the script.

### Unit Test: `test_retrieve_bitcoin_data`

The `test_retrieve_bitcoin_data` function is a unit test for the `retrieve_bitcoin_data` function. It verifies the functionality of the core data retrieval process.

```python
from src.data.pre_processor import retrieve_bitcoin_data


def test_retrieve_bitcoin_data():
    # Test case: Retrieve USD rate data for the past 1440 minutes (1 day)
    result = retrieve_bitcoin_data(rate_type='usd_rate', time_range=(1440, ))

    # Assertion: Verify that the result is not empty
    assert len(result) > 0
```

The test case retrieves USD rate data for the past 1440 minutes (1 day) using the `retrieve_bitcoin_data` function. It then asserts that the length of the result is greater than 0, indicating that data has been successfully retrieved.

Make sure to import the `retrieve_bitcoin_data` function from the appropriate module (`src.data.pre_processor`) before running the unit test.