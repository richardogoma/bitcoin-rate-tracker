"""Process data retrieval from the bitcoin rates tracker sqlite database"""

import sqlite3
import time
from config import Config

config = Config()


def retrieve_bitcoin_data(rate_type: str, time_range: tuple) -> list:
    """
    Retrieve bitcoin rate data from the database for a specific rate type and time range.

    Args:
        rate_type (str): The type of bitcoin rate to retrieve: usd_rate, gpb_rate, eur_rate.
        time_range (tuple): The time range in minutes for which to retrieve the data.

    Returns:
        list: A list of dictionaries representing the retrieved data.
    """
    start_time = time.time()
    try:
        sqlite_db_path = config.get_config_value("DATABASE_URI")

        # Establish a connection to the SQLite database
        connection = sqlite3.connect(database=sqlite_db_path)

        with connection:
            cursor = connection.cursor()

            # Query to retrieve specific rates from the 'bitcoin_rates' table
            query_string = f"""
            SELECT 
                timestamp, 
                {rate_type}
            FROM bitcoin_rates
            WHERE chart_name = 'Bitcoin' 
                AND datetime(timestamp) >= (SELECT datetime(max(timestamp), '-' || :minutes || ' minutes') FROM bitcoin_rates);
            """
            cursor.execute(query_string, {"minutes": time_range[0]})

            # Fetch the column names and map them to the retrieved rows
            columns = [column[0] for column in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        end_time = time.time()
        retrieval_time = end_time - start_time
        print(f"Data retrieval time: {retrieval_time} seconds")

        return results

    except sqlite3.Error as error_msg:
        print("Error: " + str(error_msg))

        return None

    finally:
        connection.close()
