from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='zeny_mut', # name of packe which will be package dir below project
    version='0.0.5',
    url='https://github.com/Mostafa-Elzeny/zeny_mut',
    author='Mostafa Elzeny',
    author_email='elzeny.mostafa2000@gmail.com',
    description='detect mutation in gene and its location',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["Bio"],
)