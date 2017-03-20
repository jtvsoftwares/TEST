
all: dist test install

install:
	pip install -U .

uninstall:
	pip uninstall -y jtv_test

dist:
	python setup.py bdist_wheel
	-rm -rf build
	-rm -rf jtv_test.egg-info

clean-dist:
	-rm -rf dist

test: install
	pytest

clean:
	-rm -rf .tests
	-rm -rf build
	-rm -rf jtv_test.egg-info
	-rm -f .coverage

clean-all: clean-dist clean

