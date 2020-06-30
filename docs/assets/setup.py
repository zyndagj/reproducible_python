#!/usr/bin/env python

from setuptools import setup

setup(
    name='summarize',           # package name
    version='0.0.1',            # package version
    description='A simple tool for computing the mean of a random list', # short description
    url='GitHub repo URL',      # URL for the project (optional)
    packages=["summarize"],     # Package directory
    python_requires='>=3.6,<4', # Requires a recent python3
    install_requires=[          # Runtime dependencies
        'numpy>=1,<2'
    ],
    extras_require={ #   $ pip install sampleproject[dev]
        'dev': ['pytest','tox'],
        'test': ['pytest','tox']
    },
    entry_points={              # Creates CLI scripts for accessing modules and functions
        'console_scripts': [
            'summarize=summarize:main'
        ],
    }
)
