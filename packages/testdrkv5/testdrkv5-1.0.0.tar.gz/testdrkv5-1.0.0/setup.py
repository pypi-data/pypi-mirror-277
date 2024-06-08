from setuptools import setup, find_packages

setup(
    name='testdrkv5',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "boto3 >= 1.28.10",
        "pycryptodome >= 3.20.0",
    ],
)