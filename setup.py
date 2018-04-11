# -*- coding: utf-8 -*-

import os.path
from codecs import open

from setuptools import setup

REQUIRED = [
    'h5py',
    'scipy',
    'numpy',
    'xmltodict',
    'future',
]

# find the location of this file
this_directory = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(this_directory, 'VERSION'), encoding='utf-8') as f:
    version = f.read()

setup(
    name='pymatreader',
    version=version,
    packages=['pymatreader'],
    url='https://gitlab.com/obob/pymatreader',
    license='BSD (2 clause)',
    author='Dirk Gütlin & Thomas Hartmann',
    author_email='thomas.hartmann@th-ht.de',
    description='Convenient reader for Matlab mat files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=REQUIRED,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='Matlab HDF5 import'
)
