#!/bin/bash

# Allows for seperate requirements.txt files for each branch + python version

PY=""

if [[ $TRAVIS_PYTHON_VERSION != 2.7 ]] ; then
   PY=".python3"
fi
if [ -e "requirements.${LINO_VERSION}${PY}.txt" ] ; then
    REQ="requirements.${LINO_VERSION}${PY}.txt"
else
    REQ="requirements${PY}.txt"
fi
echo "installing ${REQ}"
pip install -r ${REQ}
