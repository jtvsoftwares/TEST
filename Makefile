
all: dist test install

install:
	pip install -U .

uninstall:
	pip uninstall -y jtv_test

dist:
	python setup.py bdist_wheel
	-rm -rf build
	-rm -rf jtv_test.egg-inf

clean-dist:
	-rm -rf dist

test: install
	pip install pytest pytest-cov
	pytest

clean:
	-rm -rf .tests
	-rm -rf build
	-rm -rf jtv_test.egg-info
	-rm -f .coverage

clean-all: clean-dist clean

