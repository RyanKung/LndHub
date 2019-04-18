init_test:
	pip install -r ./tests/requirements.txt

test:
	pytest ./tests
