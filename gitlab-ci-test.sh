#!/bin/sh
cd $CI_PROJECT_DIR
pip install -U -r requirements.txt
nosetests --with-coverage --cover-package=pymatreader

tox -c tox_ci.ini