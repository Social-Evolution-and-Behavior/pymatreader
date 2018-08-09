#!/bin/sh
cd $CI_PROJECT_DIR
pip install -U -r requirements.txt
nosetests