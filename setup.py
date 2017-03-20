from setuptools import setup, find_packages

setup(
    name="jtv_test",
    version="0.0",
    packages=find_packages(exclude=['tests'])
)