#!/bin/bash

# Allows for seperate requirements.txt files for each branch + python version

PY=""

if [[ $TRAVIS_PYTHON_VERSION != 2.7 ]] ; then
   PY=".python3"
fi
if [ -e "requirements.${TRAVIS_BRANCH}${PY}.txt" ] ; then
    REQ="requirements.${TRAVIS_BRANCH}${PY}.txt"
else
    REQ="requirements${PY}.txt"
fi
echo "installing ${REQ}"
pip install -r ${REQ}
