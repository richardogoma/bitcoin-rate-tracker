-- Filename: bitcoin_rate_queries.sql

-- Schema Information Metadata
-- Retrieve the names and SQL statements of all tables in the database
SELECT name, sql
FROM sqlite_master
WHERE type = 'table'
ORDER BY name;

-- Retrieve all rows from the 'bitcoin_rates' table where the chart name is 'Bitcoin' and the timestamp is within the last 1440 minutes (24 hours)
SELECT *
FROM bitcoin_rates
WHERE chart_name = 'Bitcoin'
    AND datetime(timestamp) >= datetime('now', '-1440 minutes');

-- Retrieve the first row from the 'bitcoin_rates' table
SELECT *
FROM bitcoin_rates
LIMIT 1;

-- Retrieve the latest row from the 'bitcoin_rates' table based on the 'unique_number' column
SELECT *
FROM bitcoin_rates
ORDER BY unique_number DESC
LIMIT 1;

-- Retrieve all rows from the 'bitcoin_rates' table where the chart name is 'Bitcoin' and the timestamp is within the last 5 minutes from a specified datetime
SELECT *
FROM bitcoin_rates
WHERE chart_name = 'Bitcoin'
    AND datetime(timestamp) >= datetime('2023-06-15T17:15:00+00:00', '-5 minutes');

-- Retrieve the maximum timestamp value from the 'bitcoin_rates' table and subtract 5 minutes from it
SELECT datetime(max(timestamp), '-5 minutes')
FROM bitcoin_rates;

-- Retrieve all rows from the 'bitcoin_rates' table where the chart name is 'Bitcoin' and the timestamp is within 5 minutes of the maximum timestamp in the table
SELECT *
FROM bitcoin_rates
WHERE chart_name = 'Bitcoin'
    AND datetime(timestamp) >= (SELECT datetime(max(timestamp), '-5 minutes') FROM bitcoin_rates);

