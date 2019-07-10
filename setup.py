# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dwarf',
    version='0.0.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mauricio Panelo Jr',
    author_email='mpanelojr@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts': [
            'dwarf=dwarf.__main__:main',
        ],
    },
)
