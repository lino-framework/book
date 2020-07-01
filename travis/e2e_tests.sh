#!/bin/bash
set -ev
# E2E testing with team  TODO: move the following to the tests of the min1 project
cd lino_book/projects/avanti1/
python manage.py runserver -v 0 > /dev/null 2>&1 &
cd -
sleep 15
./node_modules/cypress/bin/cypress run -- --spec tests/cypress/integration/avanti1/* --config video=false
