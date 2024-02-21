# setup.py
from setuptools import setup, find_packages

setup(
    name='ops_test',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn==0.24.2',
        'tensorflow==2.5.0',
        'joblib==1.0.1',
        'matplotlib==3.4.2',
    ],
)