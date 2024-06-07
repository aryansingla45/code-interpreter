lint:
	pylint --disable=R,C src/*.py

format:
	black *.py

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

