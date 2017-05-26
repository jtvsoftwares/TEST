
all: dist install test

install:
	pip install -U .
	pip install mock pytest pytest-cov

uninstall:
	pip uninstall -y jtv_test

dist:
	python setup.py bdist_wheel
	-rm -rf build
	-rm -rf jtv_test.egg-inf

clean-dist:
	-rm -rf dist

test:
	py.test --junit-xml=.tests/pytest.xml --cov --cov-config=.coveragerc --cov-report=term --cov-report=html tests

clean:
	-rm -rf .tests
	-rm -rf build
	-rm -rf jtv_test.egg-info
	-rm -f .coverage

clean-all: clean-dist clean

