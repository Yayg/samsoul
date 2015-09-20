#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='samsoul',

    version='0.1',

    description='Samsoul',

    url='incoming',

    author='Rafael Gozlan',
    author_email='rafael.gozlan@epita.fr',

    license = "BSD",

    packages=['samsoul'],

    install_requires=[
        'docopt',
        'requests',
        'texttable',
        'prettytable',
    ],

    entry_points={
        'console_scripts': [
            'samsoul = samsoul.samsoul:run',
            ]
        }
)
