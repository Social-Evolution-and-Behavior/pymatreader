from distutils.core import setup

REQUIRED = [
    'h5py',
    'scipy',
    'numpy',
    'xmltodict',
]

setup(
    name='pymatreader',
    version='0.0.1',
    packages=['tests', 'tests.helper_functions'],
    url='',
    license='',
    author='Dirk Gütlin & Thomas Hartmann',
    author_email='',
    description='',
    install_requires=REQUIRED,
)
