install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src.data.pre_processor \
		tests/test_data_retrieval.py

format:
	black *.py **/*.py ***/**/*.py 

lint:
	pylint *.py **/*.py ***/**/*.py 

run:
	python3 wsgi.py

all: install format lint test run