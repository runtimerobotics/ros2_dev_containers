from setuptools import find_packages
from setuptools import setup

setup(
    name='andino_gz',
    version='0.1.1',
    packages=find_packages(
        include=('andino_gz', 'andino_gz.*')),
)
