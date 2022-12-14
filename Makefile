install:
	pip install -r requirements.txt
generate:
	python3 ./scripts/generate.py
test:
	pytest $(file:-)
