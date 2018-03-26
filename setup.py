from distutils.core import setup

REQUIRED = [
    'h5py',
    'scipy',
    'numpy',
    'xmltodict',
    'future',
]

setup(
    name='pymatreader',
    version='0.0.1',
    packages=['pymatreader'],
    url='https://gitlab.com/obob/pymatreader',
    license='GPL3',
    author='Dirk Gütlin & Thomas Hartmann',
    author_email='thomas.hartmann@th-ht.de',
    description='Convenient reader for Matlab mat files',
    long_description='Convenient reader for Matlab mat files. This package works with the <= 7 and 7.3 (i.e. HDF5) versions. A dictionary is returned, vectors and matrices are converted to numpy arrays.',
    install_requires=REQUIRED,
)
