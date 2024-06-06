from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='embedded_modbus',
    version='0.1',
    description='A simple Python library for communication with devices via modbus.',
    author='EKTOS DNE',
    packages=find_packages(),
    install_requires=required
)