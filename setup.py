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
    author_email='',
    description='Convenient reader for Matlab mat files',
    install_requires=REQUIRED,
)
