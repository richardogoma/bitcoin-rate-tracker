[![Python application](https://github.com/richardogoma/bitcoin-rate-tracker/actions/workflows/python-app.yml/badge.svg)](https://github.com/richardogoma/bitcoin-rate-tracker/actions/workflows/python-app.yml)

# Bitcoin Rate Tracker

The Bitcoin Rate Tracker is a Flask web application or microservice that allows users to track and visualize Bitcoin rates across major currencies. It provides an API for retrieving Bitcoin rates and displaying them in various time ranges.

## Project Structure
The project follows the following structure:
```bash
tree --dirsfirst --prune -I '*.pyc|__pycache__|data_streaming_client'
```

```
.
├── data
│   └── bitcoin_rate_tracker.db
├── docs
│   ├── data_retrieval.md
│   └── web_app_api.md
├── src
│   └── data
│       ├── __init__.py
│       ├── etl_client.py
│       └── pre_processor.py
├── tests
│   ├── __init__.py
│   └── test_data_retrieval.py
├── web_app
│   ├── api
│   │   └── routes.py
│   ├── home
│   │   ├── static
│   │   │   ├── highcharts
│   │   │   │   ├── stockchart.js
│   │   │   │   └── wheelchart.js
│   │   │   └── script.js
│   │   ├── templates
│   │   │   ├── highcharts
│   │   │   │   ├── stockchart.html
│   │   │   │   └── wheelchart.html
│   │   │   └── index.html
│   │   └── routes.py
│   ├── static
│   │   ├── favicon.ico
│   │   ├── logo.svg
│   │   └── style.css
│   ├── templates
│   │   └── layout.html
│   └── __init__.py
├── LICENSE
├── Makefile
├── README.md
├── config.py
├── requirements.txt
└── wsgi.py

14 directories, 27 files
```

## Setup
Typically, a virtual environment is recommended for Python projects to isolate its dependencies from your global environment. Learn more about creating virtual environments here: [Get started using Python for web development on Windows](https://learn.microsoft.com/en-us/windows/python/web-frameworks)

To set up the Flask server, edit the `config.py` file and run the following command on the terminal:
```bash
make all
```
