lint:
	pylint --disable=R,C,W0718 src/*.py

format:
	black src/*.py

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

run:
	python src/main.py

all:
	install lint format run

