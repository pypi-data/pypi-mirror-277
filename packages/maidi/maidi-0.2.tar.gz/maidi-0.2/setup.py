from setuptools import setup, find_packages
import setuptools

import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='maidi',
    version='0.2',
    author="Florian GARDIN",
    author_email="fgardin.pro@gmail.com",
    description=("A python package for symbolic AI music inference"
                 ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt", "r").read().splitlines(),
    packages=setuptools.find_packages(include='*'),
    package_data={'maidi': ['examples/*.mid', 'metadata/*.pkl']},
    include_package_data=True,
)
