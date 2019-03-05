.. _lino.dev.frontend_testing:

Testing The FrontEnd
====================

Lino uses the cypress testing module to run end to end tests.

To install and run cypress you must use npm.::

  $ npm init
  $ npm install cypress --save-dev
  $ ./node_modules/cypress/bin/cypress open

Book has some tests defined already in cypress.json.


Testing list
------------

logging in / out
inserting items
editing fields
running action
deleting
running yes-no dialog

PV filtering
