from setuptools import setup, find_packages

setup(
    name='modelslab',
    version='0.1',
    description='A package for interacting with the ModelsLab API',
    author='Sadchidananda C',
    author_email='sachith03122000@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)