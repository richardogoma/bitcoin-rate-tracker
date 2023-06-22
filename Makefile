install:
	pip install --upgrade pip && \
		pip install -r requirements.txt && \
		rm -rf data_streaming_client && \
		git clone https://github.com/richardogoma/bitcoin-rate-etl.git data_streaming_client

test:
	python -m pytest -vv --cov=src.data.pre_processor \
		tests/test_data_retrieval.py

format:
	black *.py **/*.py ***/**/*.py 

lint:
	pylint --rcfile=.pylintrc *.py **/*.py ***/**/*.py

run:
	python3 wsgi.py

all: install format lint test run