install:
	pip install --upgrade pip && \
		pip install -r requirements.txt && \

test:
	python -m pytest -vv --cov=etl.extract.data tests/test_data_retrieval.py

format:
	black *.py **/*.py ***/**/*.py 

lint:
	pylint *.py **/*.py ***/**/*.py 

run: 
	

all: install format lint test run