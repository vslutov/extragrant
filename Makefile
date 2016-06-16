SRC_DIR = extragrant
GENERATED = build dist *.egg-info

VENV_ACTIVATE = virtualenv/bin/activate

all : test lint pep257 runserver

clean :
	rm -rf $(GENERATED) **/__pycache__ **/*.pyc

test :
	py.test $(SRC_DIR)

cov :
	py.test --cov $(SRC_DIR)

lint :
	pylint $(SRC_DIR)

pep257 :
	pep257 $(SRC_DIR)

runserver : $(VENV_ACTIVATE)
	( \
		source $(VENV_ACTIVATE) && \
		python extragrant/manage.py runserver 127.0.0.1:8000 \
	)

$(VENV_ACTIVATE) :
	( \
		virtualenv virtualenv && \
		source $(VENV_ACTIVATE) && \
		pip install -r requirements.txt \
	)
