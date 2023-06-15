SELECT name, sql FROM sqlite_master
WHERE type='table'
ORDER BY name;

SELECT 
    timestamp, 
    usd_rate
FROM bitcoin_rates
WHERE chart_name == 'Bitcoin'
    AND datetime(timestamp) >= datetime('now', '-1440 minutes');

SELECT 
    *
FROM bitcoin_rates
WHERE chart_name == 'Bitcoin'
    AND datetime(timestamp) >= datetime('now', '-1440 minutes');