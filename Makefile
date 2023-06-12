install:
	pip install --upgrade pip && \
		pip install -r requirements.txt && \

test:
	python -m pytest -vv --cov=etl.extract.retriever --cov=etl.transform.parser \
		tests/test_data_retrieval.py tests/test_data_parsing.py

format:
	black *.py **/*.py ***/**/*.py 

lint:
	pylint *.py **/*.py ***/**/*.py 

run: 
	

all: install format lint test run