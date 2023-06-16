# Bitcoin Rate Tracker

The Bitcoin Rate Tracker is a Flask web application or microservice that allows users to track and visualize Bitcoin rates across major currencies. It provides an API for retrieving Bitcoin rates and displaying them in various time ranges.

## Project Structure
The project follows the following structure:

```
.
├── data
│   └── bitcoin_rate_tracker.db
├── docs
│   ├── data_retrieval.md
│   └── web_app_api.md
├── src
│   └── data
│       ├── __init__.py
│       ├── pre_processor.py
│       └── test_scripts.sql
├── tests
│   ├── __init__.py
│   └── test_data_retrieval.py
├── web_app
│   ├── api
│   │   └── routes.py
│   ├── home
│   │   └── routes.py
│   └── __init__.py
├── LICENSE
├── Makefile
├── README.md
├── config.py
├── requirements.txt
└── wsgi.py
```

## Setup
To set up the Flask server, run the following command:
```bash
make all
```

## Usage
To access the Bitcoin rates, use the following URL with appropriate parameters:
```
http://127.0.0.1:5051/data?currency=<currency_code>&timerange=<time_range>
```
Replace `<currency_code>` with the desired currency code (e.g., USD, EUR) and `<time_range>` with the desired time range (e.g., 1h, 24h).

For more detailed information on data retrieval and the web app API, refer to the documentation files located in the `docs` directory.